#!/usr/bin/env python3
"""
SCRIPT PÉDAGOGIQUE — MOISSONNAGE AVEC SELENIUM 4

Ce programme procède au moissonnage d'une page OpenEdition. 
Il garde volontairement une structure lisible : 
configuration → navigateur → page → HTML brut → métadonnées →
aperçu de texte → traces de provenance.

EXEMPLE PAR DÉFAUT
    https://journals.openedition.org/aad/171

PLACE DANS LE DÉPÔT
    chaine/03_acquisition/exemple/01_moissonnage_selenium_exemple.py

ATTENTION
    - Il s'agit d'un exemple pédagogique portant sur UNE URL explicite.
    - Il ne découvre pas automatiquement des liens et ne télécharge pas
      automatiquement de PDF.
    - Il ne remplace pas le protocole d'acquisition du projet.
    - Vérifier les conditions d'accès, de réutilisation et de redistribution.
    - robots.txt n'est pas une autorisation juridique de collecte.
    - Ne pas transmettre de données sensibles, privées ou sous licence
      restrictive à un service externe sans autorisation.

À lire avant exécution
    chaine/03_acquisition/README.md
    donnees/README.md
    configuration/README.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# 1. Bibliothèques de la bibliothèque standard
# ---------------------------------------------------------------------------
import argparse
import csv
import hashlib
import json
import logging
import sys
import time
import urllib.robotparser
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

# ---------------------------------------------------------------------------
# 2. Bibliothèques installées dans l'environnement Python du projet
# ---------------------------------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ---------------------------------------------------------------------------
# 3. Chemins relatifs au dépôt Git
# ---------------------------------------------------------------------------
# Le script est supposé se trouver dans :
# root/chaine/03_acquisition/exemple/01_moissonnage_selenium_exemple.py
# parents[3] correspond donc au dossier racine du projet.
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# URL par defaut
DEFAULT_URL = "https://journals.openedition.org/aad/171"

# Sélecteurs CSS génériques. L'étudiant doit les vérifier avec l'inspecteur
# du navigateur et les adapter au site réellement étudié.
DEFAULT_CONTENT_SELECTOR = "#content, article, main"
DEFAULT_PDF_SELECTOR = "a.dlpdf, a[href$='.pdf']"


# ---------------------------------------------------------------------------
# 4. Arguments de ligne de commande
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ouvre une page avec Selenium, conserve le HTML brut et produit un aperçu pédagogique."
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"URL à consulter. Exemple pédagogique par défaut : {DEFAULT_URL}",
    )
    parser.add_argument(
        "--id-document",
        default="D0001",
        help="Identifiant stable du document, par exemple D0001.",
    )
    parser.add_argument(
        "--id-source",
        default="S001",
        help="Identifiant stable de la source, par exemple S001.",
    )
    parser.add_argument(
        "--content-selector",
        default=DEFAULT_CONTENT_SELECTOR,
        help="Sélecteur CSS du contenu principal ; à vérifier pour chaque source.",
    )
    parser.add_argument(
        "--pdf-selector",
        default=DEFAULT_PDF_SELECTOR,
        help="Sélecteur CSS facultatif pour repérer un lien PDF ; le script enregistre seulement son URL.",
    )
    parser.add_argument(
        "--sources-dir",
        type=Path,
        default=PROJECT_ROOT / "donnees" / "sources",
        help="Dossier des pages HTML sources brutes.",
    )
    parser.add_argument(
        "--intermediate-dir",
        type=Path,
        default=PROJECT_ROOT / "donnees" / "intermediaires",
        help="Dossier des métadonnées et aperçus intermédiaires.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=PROJECT_ROOT / "chaine" / "03_acquisition" / "logs" / "selenium_acquisition.log",
        help="Journal technique de l'exécution.",
    )
    parser.add_argument(
        "--user-agent",
        default="LanguesDeSpecialiteCours/1.0",
        help="User-Agent transmis à Chrome. Ajouter un contact pour un projet réel si approprié.",
    )
    parser.add_argument(
        "--robot-agent",
        default="LanguesDeSpecialiteCours",
        help="Nom utilisé pour la vérification de robots.txt.",
    )
    parser.add_argument(
        "--wait-seconds",
        type=int,
        default=15,
        help="Temps maximal d'attente d'un élément de page.",
    )
    parser.add_argument(
        "--inspect-seconds",
        type=int,
        default=0,
        help="Temps pendant lequel garder la page ouverte après collecte pour permettre l'inspection manuelle.",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Lance Chrome sans fenêtre. Laisser désactivé pendant la formation afin d'observer le navigateur.",
    )
    parser.add_argument(
        "--terms-reviewed",
        action="store_true",
        help="Confirme que les conditions d'accès, de collecte et de réutilisation ont été examinées.",
    )
    parser.add_argument(
        "--ignore-robots",
        action="store_true",
        help="Désactive le contrôle robots.txt. Cette dérogation doit être autorisée et justifiée dans le journal.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Autorise le remplacement des fichiers de sortie existants.",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# 5. Journal technique
# ---------------------------------------------------------------------------
def configure_logging(log_file: Path) -> None:
    """Écrit les événements dans un fichier et les affiche dans le terminal."""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler()],
    )


# ---------------------------------------------------------------------------
# 6. Vérification technique de robots.txt
# ---------------------------------------------------------------------------
def check_robots(url: str, robot_agent: str) -> bool | None:
    """
    Retourne :
        True  : robots.txt permet techniquement la consultation.
        False : robots.txt l'interdit.
        None  : robots.txt n'a pas pu être lu.

    None n'est PAS une permission implicite. La décision doit être prise
    selon le protocole et les conditions de la source.
    """
    parsed = urlparse(url)
    robots_url = urljoin(f"{parsed.scheme}://{parsed.netloc}", "/robots.txt")
    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(robots_url)
    try:
        parser.read()
        allowed = parser.can_fetch(robot_agent, url)
        logging.info("robots.txt : %s | autorisation technique : %s", robots_url, allowed)
        return allowed
    except Exception as exc:
        logging.warning("robots.txt non vérifiable (%s) : %s", robots_url, exc)
        return None


# ---------------------------------------------------------------------------
# 7. Fonctions de lecture des métadonnées HTML
# ---------------------------------------------------------------------------
def meta_content(soup: BeautifulSoup, *names: str) -> str | None:
    """Retourne le premier contenu de balise meta correspondant à un nom."""
    for name in names:
        tag = soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
        tag = soup.find("meta", attrs={"property": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None


def all_meta_content(soup: BeautifulSoup, *names: str) -> list[str]:
    """Retourne toutes les valeurs de meta correspondant aux noms fournis."""
    values: list[str] = []
    for name in names:
        for tag in soup.find_all("meta", attrs={"name": name}):
            if tag.get("content"):
                values.append(tag["content"].strip())
        for tag in soup.find_all("meta", attrs={"property": name}):
            if tag.get("content"):
                values.append(tag["content"].strip())
    return list(dict.fromkeys(values))


# ---------------------------------------------------------------------------
# 8. Extraction PÉDAGOGIQUE d'un aperçu de texte
# ---------------------------------------------------------------------------
def extract_preview(soup: BeautifulSoup, selector: str) -> str:
    """
    Produit un aperçu à des fins pédagogiques.

    La sortie ne doit pas être traitée comme le corpus préparé final :
    l'extraction et le nettoyage stabilisés appartiennent à l'étape 04.
    """
    container = soup.select_one(selector)
    if container is None:
        return ""
    paragraphs = container.select("p")
    lines = [paragraph.get_text(" ", strip=True) for paragraph in paragraphs]
    return "\n\n".join(line for line in lines if line)


# ---------------------------------------------------------------------------
# 9. Enregistrement des sorties
# ---------------------------------------------------------------------------
def write_json(path: Path, data: dict, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Fichier existant : {path}. Utiliser --overwrite après vérification.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def append_acquisition_csv(path: Path, row: dict) -> None:
    """Ajoute une ligne de provenance sans modifier l'inventaire final du corpus."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(row.keys())
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


# ---------------------------------------------------------------------------
# 10. Programme principal : étapes visibles dans Chrome et dans les fichiers
# ---------------------------------------------------------------------------
def main() -> int:
    args = parse_args()

    if not args.terms_reviewed:
        print(
            "Refus : ajoutez --terms-reviewed seulement après avoir vérifié les conditions "
            "d'accès, de collecte, de réutilisation et de redistribution.",
            file=sys.stderr,
        )
        return 2

    if urlparse(args.url).scheme not in {"http", "https"}:
        print("Erreur : --url doit commencer par http:// ou https://", file=sys.stderr)
        return 2

    configure_logging(args.log_file)
    logging.info("Projet : %s", PROJECT_ROOT)
    logging.info("Document : %s | URL : %s", args.id_document, args.url)

    # Étape 10.1 : vérification technique robots.txt.
    robots_allowed = None
    if not args.ignore_robots:
        robots_allowed = check_robots(args.url, args.robot_agent)
        if robots_allowed is not True:
            logging.error("Collecte interrompue : robots.txt interdit ou ne permet pas de vérifier cette consultation.")
            logging.error("Documenter toute décision différente dans le journal et le protocole.")
            return 3
    else:
        logging.warning("Contrôle robots.txt désactivé. Justification obligatoire dans le journal.")

    # Étape 10.2 : définir les fichiers produits.
    raw_html_path = args.sources_dir / f"{args.id_document}_source.html"
    metadata_path = args.intermediate_dir / f"{args.id_document}_metadonnees.json"
    preview_path = args.intermediate_dir / f"{args.id_document}_apercu_texte.txt"
    acquisition_csv = args.intermediate_dir / "metadata_acquisition.csv"

    if not args.overwrite:
        existing = [path for path in (raw_html_path, metadata_path, preview_path) if path.exists()]
        if existing:
            logging.error("Fichier(s) déjà présent(s) : %s", ", ".join(str(path) for path in existing))
            logging.error("Vérifier les fichiers ou utiliser --overwrite après décision documentée.")
            return 4

    # Étape 10.3 : préparer les options Chrome.
    options = Options()
    options.add_argument(f"--user-agent={args.user_agent}")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-notifications")
    if args.headless:
        options.add_argument("--headless=new")

    # Selenium Manager gère normalement le pilote compatible avec Chrome.
    # Aucun chemin local vers chromedriver.exe n'est codé dans le script.
    driver = None
    timestamp = datetime.now(UTC).isoformat()

    try:
        # Étape 10.4 : démarrer un navigateur Chrome contrôlé par Selenium.
        driver = webdriver.Chrome(options=options)

        # Étape 10.5 : charger la page demandée.
        driver.get(args.url)

        # Étape 10.6 : attendre explicitement le body plutôt que dormir arbitrairement.
        wait = WebDriverWait(driver, args.wait_seconds)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Étape 10.7 : conserver l'URL finale et le titre après redirections éventuelles.
        final_url = driver.current_url
        page_title = driver.title
        html = driver.page_source
        html_bytes = html.encode("utf-8")
        sha256 = hashlib.sha256(html_bytes).hexdigest()

        # Étape 10.8 : enregistrer une copie brute de la page HTML.
        raw_html_path.parent.mkdir(parents=True, exist_ok=True)
        raw_html_path.write_text(html, encoding="utf-8")
        logging.info("HTML brut enregistré : %s", raw_html_path)

        # Étape 10.9 : analyser le HTML enregistré afin d'illustrer les métadonnées.
        soup = BeautifulSoup(html, "html.parser")
        authors = all_meta_content(soup, "citation_author", "DC.creator", "DC.contributor")

        # Étape 10.10 : repérer éventuellement un lien PDF, sans le télécharger.
        pdf_url = None
        pdf_candidates = driver.find_elements(By.CSS_SELECTOR, args.pdf_selector)
        if pdf_candidates:
            pdf_url = pdf_candidates[0].get_attribute("href")

        metadata = {
            "id_document": args.id_document,
            "id_source": args.id_source,
            "url_demandee": args.url,
            "url_finale": final_url,
            "date_collecte_utc": timestamp,
            "titre_navigateur": page_title,
            "titre_meta": meta_content(soup, "DC.title", "citation_title", "og:title"),
            "auteurs": authors,
            "date_publication": meta_content(soup, "DC.date", "citation_publication_date", "article:published_time"),
            "langue": meta_content(soup, "DC.language", "citation_language", "og:locale"),
            "doi": meta_content(soup, "citation_doi", "DC.identifier", "DOI"),
            "resume": meta_content(soup, "citation_abstract", "DC.description", "description"),
            "mots_cles": all_meta_content(soup, "keywords", "citation_keywords", "DC.subject"),
            "pdf_url_reperee": pdf_url,
            "selector_contenu": args.content_selector,
            "robots_allowed": robots_allowed,
            "user_agent": args.user_agent,
            "fichier_html_source": str(raw_html_path.relative_to(PROJECT_ROOT)),
            "sha256_html": sha256,
            "octets_html": len(html_bytes),
            "statut": "collecte_pedagogique_reussie",
        }
        write_json(metadata_path, metadata, args.overwrite)
        logging.info("Métadonnées enregistrées : %s", metadata_path)

        # Étape 10.11 : produire un aperçu de texte pour montrer le parsing HTML.
        # Cette sortie est intermédiaire ; le protocole d'extraction définitif
        # doit être réalisé et contrôlé dans 04_preparation/01_extraction/.
        preview = extract_preview(soup, args.content_selector)
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        preview_path.write_text(preview, encoding="utf-8")
        logging.info("Aperçu de texte enregistré : %s", preview_path)

        # Étape 10.12 : ajouter une trace de provenance à un CSV d'acquisition.
        append_acquisition_csv(
            acquisition_csv,
            {
                "id_document": args.id_document,
                "id_source": args.id_source,
                "url_demandee": args.url,
                "url_finale": final_url,
                "date_collecte_utc": timestamp,
                "titre": metadata["titre_meta"] or page_title,
                "langue": metadata["langue"] or "",
                "doi": metadata["doi"] or "",
                "pdf_url_reperee": pdf_url or "",
                "fichier_html_source": str(raw_html_path.relative_to(PROJECT_ROOT)),
                "fichier_metadonnees": str(metadata_path.relative_to(PROJECT_ROOT)),
                "fichier_apercu": str(preview_path.relative_to(PROJECT_ROOT)),
                "sha256_html": sha256,
                "robots_allowed": robots_allowed,
                "statut": "collecte_pedagogique_reussie",
            },
        )

        print("\nCollecte pédagogique terminée.")
        print(f"HTML brut      : {raw_html_path}")
        print(f"Métadonnées    : {metadata_path}")
        print(f"Aperçu texte   : {preview_path}")
        print(f"PDF repéré     : {pdf_url or 'aucun lien trouvé'}")
        print("\nÉtape suivante : vérifier les fichiers, puis définir l'extraction stabilisée dans 04_preparation.")

        # Étape 10.13 : garder Chrome ouvert si l'enseignant veut montrer le DOM.
        if args.inspect_seconds > 0 and not args.headless:
            logging.info("Inspection manuelle : attente de %s seconde(s).", args.inspect_seconds)
            time.sleep(args.inspect_seconds)

    except TimeoutException:
        logging.exception("Temps d'attente dépassé : vérifier l'URL ou le sélecteur.")
        return 5
    except WebDriverException:
        logging.exception("Erreur Selenium : vérifier Chrome, Selenium et Selenium Manager.")
        return 6
    except Exception:
        logging.exception("Erreur inattendue pendant la collecte.")
        return 7
    finally:
        # Étape 10.14 : fermer le navigateur, même en cas d'erreur.
        if driver is not None:
            driver.quit()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
