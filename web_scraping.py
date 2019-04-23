
# coding: utf-8

# In[3]:


import time, requests
import pandas as pd
from bs4 import BeautifulSoup as bs
#Be nice and fill in the headers below with your real info. When web scraping, make it easier for the website administrator 
#identify you if the needs to
headers = {
    'user-agent': 'your_name',
    'from': 'your_email'
}

