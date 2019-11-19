
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib as mplPorterStemmer
import collections
from scipy import stats
from statsmodels import stats as stat


# In[47]:


user = pd.read_csv('user.csv')
user.head()


# In[48]:


tip = pd.read_csv('tip.csv')
tip.head()


# In[49]:


ice = pd.read_csv('ice.csv')
ice.head()


# In[50]:


len(ice)


# In[51]:


review = pd.read_csv('review.csv')
review.head()


# In[52]:


len(review)


# In[53]:


str2 = 'topping, cookie, waffle, crunch, sugar, diary, homemade, custard, price, cheap, expensive, quality, wait, employee, manager, texture, fan, vanilla, chocolate, strawberry, peanut, oreo, caramel, delicious, friendly, small, little, big, fresh, creamy, hard, park, located, location'
str2 = str2.split(', ')


# In[54]:

## Indicator  whether each review contains above words
all_word = review.copy()
for i in str2:
    a=review.text.str.contains(i).apply(lambda x: 1 if x is True else 0)
    all_word[i]=a


# In[62]:


import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from mlxtend.plotting import plot_decision_regions


tree = DecisionTreeClassifier(criterion='entropy', 
                              max_depth=3, 
                              random_state=1)
tree.fit(all_word.loc[:,flavor], review.stars)


# In[64]:

#Train Decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz


dot_data = export_graphviz(tree,
                           filled=True, 
                           rounded=True,
                           class_names=['0', '1','2','3','4','5'],
                           feature_names=flavor,
                           out_file=None) 
graph = graph_from_dot_data(dot_data) 
graph.write_png('tree.png')# SHow the graph


# Noun:
# about ice cream: topping, cookie, waffle, crunch, sugar, homemade, 
# 
# about service: price, quality, wait, employee, texture, fan
# 
# Flavor: vanilla, chocolate, strawberry, peanut, oreo, caramel
# 
# Adj:
# delicious, friendly, small/little/big, fresh, creamy, hard
# 
# Verb:
# parking, located, location

# In[13]:


flavor = 'vanilla,chocolate,strawberry,peanut,oreo,caramel,custard,waffle,cookie,topping,sugar,creamy'
properties = 'homemade,crunch,quality,texture,small,big,fresh,delicious'
service =  'location,park,friendly,fan,employee,manager,wait,price,expensive'


# In[14]:


flavor = flavor.split(',')
properties = properties.split(',')
service = service.split(',')


# In[16]:


all_word = review.copy()
for i in str2:
    a=review.text.str.contains(i).apply(lambda x: 1 if x is True else 0)
    all_word[i]=a


# In[17]:

#Connect the words frequency with star
all_count = all_word.loc[:,str2].groupby(all_word.stars).sum()


# In[18]:


all_count['small'] += all_count['little']
all_count['location'] += all_count['located']


# In[19]:


all_count.drop(['little','located','diary'], axis = 1, inplace=True)


# In[21]:


all_count


# In[70]:


stats.chisquare(all_count.iloc[:,1],prop1)


# In[79]:


for i in range(31):
    print(stats.chisquare(all_count.iloc[:,i],prop1*( 5te4s2wall_count.iloc[:,i].sum())))


# In[28]:

#Plot heatmap for words-frequency
ax_log = sns.heatmap(all_count1.loc[:,flavor])
plt.title('Words - stars frequency_flavor')
plt.xlabel('words')
plt.ylabel('Stars')


# In[41]:


ax_log = sns.heatmap(all_count1.loc[:,properties])
plt.title('Words - stars frequency_properties')
plt.xlabel('words')
plt.ylabel('Stars')


# In[42]:


ax_log = sns.heatmap(all_count1.loc[:,service])
plt.title('Words - stars frequency_properties')
plt.xlabel('words')
plt.ylabel('Stars')

