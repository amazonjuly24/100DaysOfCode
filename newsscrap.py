
# coding: utf-8

# In[32]:


import requests
from bs4 import BeautifulSoup


# In[33]:


url='https://www.hindustantimes.com/rss/topnews/rssfeed.xml'


# In[34]:


resp=requests.get(url)


# In[35]:


soup=BeautifulSoup(resp.content, features='xml')


# In[41]:


print(soup.prettify())


# In[43]:


items=soup.findAll('item')


# In[44]:


len(items)


# In[45]:


item=items[0]


# In[49]:


item
news_items=[]


# In[52]:


for item in items:
    news_item={}
    news_item['title']=item.title.text
    #news_item['description']=item.description.text
    news_item['link']=item.link.text
    #news_item['image']=item.content['url']
    news_items.append(news_item)


# In[54]:


news_items[0]

