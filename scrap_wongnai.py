#!/usr/bin/env python
# coding: utf-8

# In[212]:


from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# In[ ]:


loc_titles_list = []
loc_rating_list = []
loc_review_list = []
loc_location_list = []


# In[213]:


for page in range(1, 40):
    # Set the path to your Chrome WebDriver executable
    chrome_driver_path = r'C:\Users\jira\dsi464/chromedriver.exe'
    # Create a ChromeOptions object
    options = webdriver.ChromeOptions()

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    
    url = f'https://www.wongnai.com/businesses?categories=4411&categories=4416&page.size=10&rerank=false&domain=4&page.number={page}'
    driver.get(url)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    
    loc_titles = soup.find_all('h2', {'class':'sc-1qge0b2-0 kfaqPY bd20'})
    loc_rating = soup.find_all('div', {'class':'Gap-sc-ilei7b Container-sc-1lk8ybd ikRntG bZDAts badge-content badge-content'})
    loc_review = soup.find_all('span', {'class':'sc-1uyabda-0 iQqWsz rg12 text-gray-500'})
    loc_location = soup.find_all('div', {'class':'text-gray-500'})
    
    for location in loc_location:
        loc_location_list.append(location.text)
        
    for review in loc_review:
        loc_review_list.append(review.text)
        
    for titles in loc_titles:
            loc_titles_list.append(titles.text)
            
    for rating in loc_rating:
        loc_rating_list.append(rating.text)
        
    driver.quit()

loc_titles_list 
loc_rating_list
loc_review_list
loc_location_list


# In[214]:


pd.set_option('display.max_colwidth', 5000)
pd.set_option('max_rows', None)


# In[215]:


table = pd.DataFrame([loc_titles_list,loc_rating_list,loc_review_list,loc_location_list]).transpose()
table.columns = ['name','rating','review','location']
table


# In[217]:


df = table
df.to_csv('C:\\Users\\jira\\dsi464\\scrap_wongnai.csv')


# In[216]:


#loc_location_list = []



#chrome_driver_path = r'C:\Users\jira\dsi464/chromedriver.exe'

#options = webdriver.ChromeOptions()


#driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    
#url = f'https://www.wongnai.com/businesses?categories=4411&categories=4416&page.size=10&rerank=false&domain=4&page.number=1'
#driver.get(url)
#data = driver.page_source
#soup = bs4.BeautifulSoup(data)
    
#loc_location = soup.find_all('div', {'class':'text-gray-500'})
#for location in loc_location:
   #     loc_location_list.append(location.text)
    
    
#loc_location_list 


# In[ ]:




