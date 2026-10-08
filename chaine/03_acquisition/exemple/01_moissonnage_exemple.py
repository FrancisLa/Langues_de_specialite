# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Tue Jan  7 18:21:21 2020
@author: Francis Lareau
Introduction to text mining with Python, Scrapping
"""
#==============================================================================
# ############################################################## Import library
#==============================================================================

# Import basic library
import os
import pandas as pd
import pickle
import re
import numpy as np

# Import specific library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import time
from bs4 import BeautifulSoup
import PyPDF2

#==============================================================================
# #################################################### Initialize project paths
#==============================================================================

root = 'C:\\'
main_path = os.path.join(root,'Formation')
os.chdir(main_path)
project_name='Formation'

#==============================================================================
# ################################################################# Preparation
#==============================================================================

# Scrapping path
scrapping_name='Moissonnage'
scrapping_output=os.path.join(main_path,scrapping_name,"PDF")

#Driver path
path_webDriver = "C:\\Chromedriver\\chromedriver.exe"

#Create a DataFrame
DF = pd.DataFrame(columns=['Date','Volume','Issue','Article_ID','Author','Title',
                           'Abstract','Keywords','Article','Footnotes','References',
                           'Page_range','Language','Journal','DOI','Type','XML','TXT'])

#Selenium configuration (profile options for pdf download)
options = webdriver.ChromeOptions()
profile = {"plugins.plugins_list": [{"enabled": False,"name": "Chrome PDF Viewer"}],
           "download.default_directory": scrapping_output,
           "download.extensions_to_open": ""}
options.add_experimental_option("prefs", profile)

#==============================================================================
# ################################################################### Execution
#==============================================================================

# Open Chrome and go to web page
url = "https://journals.openedition.org/aad/171"
driver = webdriver.Chrome(path_webDriver,chrome_options = options)
driver.get(url)

###############################################################################
#              Use Ctrl+U or F12 in browser to see html code                  #
#         Select the Elements tab at the top of the right window or           #
#            Right-click on a blank part of the web page and                  #
#          select View source from the pop-up menu that appears               #
#                                                                             #
#                 https://fr.wikipedia.org/wiki/XPath                         #
#                  Exemple: .//article[@nom='XPath']	                      #
#    sélectionne tous les éléments "article" du document où qu'ils soient,    # 
#           ayant un attribut "nom" dont la valeur est "XPath"                #
###############################################################################

# Since some pdf aren't available, try and except was added to the code below

while True:
    articles = re.findall('(?<=title"\>\<a href=")\d+(?="\>)',driver.page_source) #get articles href
    for article in articles:
        driver.find_element_by_xpath(('.//a[@href="'+article+'"]')).click() #get article
        time.sleep(2)
        ## initialise row dataframe
        n_id = DF.shape[0]
        DF.loc[n_id]= list(np.repeat('', len(DF.columns.values)))
        ## get html content
        DF.loc[n_id]['XML'] = driver.page_source #get html        
        try: #to download associated pdf
            driver.find_element_by_id('dlLinks').click() #popup menu
            driver.find_element_by_xpath('.//a[@class="dl dlpdf"]').click() #pdf download
            time.sleep(10)
            #rename last file downloaded
            last_file = max(glob.iglob(os.path.join(scrapping_output,'*')),
                            key=os.path.getctime)
            os.rename(last_file,os.path.join(scrapping_output, str(n_id)+'.pdf'))
        except:
            pass        
        driver.back()
        time.sleep(2)
    driver.find_element_by_xpath('.//a[@class="goNext"]').click() #next issue
    time.sleep(2)

#==============================================================================
# ############################################################ Extract Metadata
#==============================================================================

###############################################################################
# soup.find trouve le premier element, soup.find_all trouve tous les éléments #
#                Exemple: soup.find('article', {"nom":"XPath"})	              #
#    sélectionne le premier élément "article" du document où qu'il soit,      # 
#             ayant un attribut "nom" dont la valeur est "XPath"              #
###############################################################################

#get metadata from html            
for i in range(0,len(DF)):
    soup=BeautifulSoup(DF.XML[i],'html')
    DF.Title[i]=soup.find('meta', {"name": "DC.title"}).get('content')
    #DF.Type[i]=soup.find_all('meta', {"name": "DC.type"})[1].get('content')
    DF.Type[i]=soup.find('meta', {"property": "og:type"}).get('content')
    try:
        DF.DOI[i]=soup.find('meta', {"scheme": "DOI"}).get('content')
    except:
        DF.DOI[i]==''
    DF.Language[i]=soup.find('meta', {"name": "DC.language"}).get('content')
    DF.Date[i]=soup.find('meta', {"name": "DC.date"}).get('content')
    DF.Volume[i]=soup.find('meta', {"name": "citation_issue"}).get('content')
    authors=[]
    for author in soup.find('meta', {"name": "citation_authors"}).get('content').split('; '):
        if author=='no author':
            (a,b)=('','')
        else:
            (a,b)=author.split(', ')
        authors.append((a,b))
    DF.Author[i]=authors
    try:
        DF.Keywords[i]=soup.find('meta', {"name": "keywords"}).get('content').split(', ')
    except:
        DF.Keywords[i]=[]
    try:
        DF.Abstract[i]=re.sub('\xa0',' ',soup.find('meta', {"name": "citation_abstract"}).get('content'))
    except:
        DF.Abstract[i]=''

#==============================================================================
# ###################################################### Extract Data from html
#============================================================================== 

for i in range(0,len(DF)):
    soup=BeautifulSoup(DF.XML[i],'html')
    article=''
    for para in soup.find_all('p', {"class": "texte"}):
        para=re.sub('^\d+','',para.text)
        article=article+para+'\n\n'
    article=re.sub('\xa0',' ',article) # delet non-breaking space
    DF.Article[i]=article

#from lxml import etree as LET
#for i in range(len(DF)):
#    tree = LET.parse("doc/test.xml") 
#    article=''   
#    for para in tree.xpath('//p[@class="texte"]/descendant-or-self::*/text()'):
#        para=re.sub('^\d+','',para)
#        article=article+para+'\n\n'
#        article=re.sub('\xa0',' ',article) # delet non-breaking space
#        DF.Article[i]=article
    
#==============================================================================
# ####################################################### Extract Data from PDF
#============================================================================== 

for i in range(0,len(DF)):
    pdfFileObj = open(os.path.join(main_path,scrapping_name,"PDF",str(i)+'.pdf'), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    article=''
    for page in range(0,pdfReader.numPages):
        article = article+pdfReader.getPage(page).extractText()+'\r\n'
    DF.TXT[i]=article
    pdfFileObj.close()

#==============================================================================
# ################################################################## Rename PDF
#==============================================================================

path=os.path.join(main_path,scrapping_name,"PDF")
for i in range(0,len(DF)):
    os.rename(os.path.join(path,str(i)+'.pdf'),
              os.path.join(path,re.sub('/','%',DF.DOI[i])+'.pdf')) 

#==============================================================================
# ############################################################# Export and save
#==============================================================================
    
chemin_output=os.path.join(main_path,scrapping_name,project_name+'_'+scrapping_name)
pd.to_pickle(DF,chemin_output+".pkl")
writer = pd.ExcelWriter(chemin_output+".xlsx")
DF.to_excel(writer,'Sheet1')
writer.save()
    