#!/usr/bin/env python
# coding: utf-8

# # riot-api-test
# 
# Use the "Run" button to execute the code.

# In[224]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[5]:


import jovian
import requests
from statistics import mean
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"]=20,20


# In[6]:


# Execute this to save new versions of the notebook
jovian.commit(project="riot-api-test")


# In[7]:


requests.get("https://na1.api.riotgames.com/tft/league/v1/challenger?api_key=<RIOT_API_KEY_HERE>")


# In[8]:


response = requests.get("https://na1.api.riotgames.com/tft/league/v1/challenger?api_key=<RIOT_API_KEY_HERE>")
data = response.json()
print(data)


# In[9]:


entries = data["entries"]


# In[14]:


for entry in entries:
    print(entry)


# In[15]:


results = {}
for entry in entries:
    total = entry['wins'] + entry['losses']
    winLoss = entry['wins']/total * 100
    results[entry["summonerName"]] = winLoss

print(results)


# In[16]:


# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
        
# get results from api and sort
results = sorted(results.items(), key=lambda x: x[1], reverse=True)
names = list()
values = list()

for index, tup in enumerate(results):
    element_one = tup[0]
    element_two = tup[1]
    names.append(element_one)
    values.append(element_two)

# Avg challenger win rate
avg = mean(values)
avg = round(avg,2)
print("This is the overall average in challenger elo: {}".format(avg))
    
# Top 20 players' win rates    
# plt.bar(range(len(results)), values, tick_label=names)
print()
print("This is the top 20 win rates in challenger elo, win rate with respect to win loss percentage")
plt.figure()

names=names[:20]
values=values[:20]
values_rounded = [round(num, 1) for num in values]

# Graph Edits
ax = plt.gca()
ax.tick_params(axis='x', labelrotation = 45)
plt.bar(range(20), values_rounded, tick_label=names)

# giving title to the plot
plt.title("Top 20 Win Rates in Challenger Elo")

# calling the function to add value labels
addlabels(names, values_rounded)

# giving X and Y labels
plt.xlabel("Summoner IGN")
plt.ylabel("Win Rate Percent")

plt.show()
print ("Not sure how to remove the scroll in jovian output, b/c it's removed in jupyterhub using binder")


# In[ ]:





# In[ ]:





# In[ ]:




