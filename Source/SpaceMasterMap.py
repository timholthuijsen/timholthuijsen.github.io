#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the pandas library
import pandas as pd
# import the map library
import folium
#for getting the google sheet
import requests


# In[2]:


#different map themes at: https://deparkes.co.uk/2016/06/10/folium-map-tiles/

# Make an empty map
m = folium.Map(location=[52.132633,5.291266], tiles="openstreetmap", zoom_start=4)

# Show the map
m


# In[3]:


import requests
import os

sheet_id = "1bV4WUZNM4LBBeQutiQXLa_JhxoFIE7rHnGCG4Ili7LY"
gid = "0"

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

save_path = "WhereAreYou.csv"

resp = requests.get(url)
resp.raise_for_status()

with open(save_path, "wb") as f:
    f.write(resp.content)

print("Saved:", save_path)


# In[4]:


data = pd.read_csv('WhereAreYou.csv')
print(data)


# In[5]:


# Make a data frame with dots to show on the map
data = pd.read_csv('WhereAreYou.csv')

for i, naam in enumerate(data['Name']):
    try:
        float(data['Latitude'][i])
        boolean = True
    except:
        boolean = False

# Keep only rows where Name, Latitude, and Longitude are present
required_cols = ['Name', 'Latitude [deg]', 'Longitude [deg]']
data = data.dropna(subset=required_cols)
data


# In[6]:


# add marker one by one on the map
for i in range(0,len(data)):
    folium.Marker(
      location=[data.iloc[i]['Latitude [deg]'], data.iloc[i]['Longitude [deg]']],
      popup=data.iloc[i]['Name'],
    ).add_to(m)

# Show the map again
m


# In[7]:


m.save('index.html')


# In[ ]:




