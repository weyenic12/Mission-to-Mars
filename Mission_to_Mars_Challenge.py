#!/usr/bin/env python
# coding: utf-8

# In[128]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[129]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[53]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[54]:


slide_elem.find('div', class_='content_title')


# In[55]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[56]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[60]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[61]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[62]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[63]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[64]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[65]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[66]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[67]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[143]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[144]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
#items = browser.find_by_css('a.product-item h3')
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    mars_hemispheres = {}
    img = browser.find_by_tag('h3')[i]
    img.click()
    html = browser.html
    web_soup = soup(html, 'html.parser')
    img_link = browser.links.find_by_text('Sample').first
    mars_hemispheres['img_url'] = img_link['href']
    img_title = web_soup.find('h2', class_='title').get_text()
    mars_hemispheres['title'] = img_title
    hemisphere_image_urls.append(mars_hemispheres)
    browser.back()


# In[145]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[146]:


# 5. Quit the browser
browser.quit()


# In[ ]:




