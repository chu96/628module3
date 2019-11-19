
# coding: utf-8

# In[1]:


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


# In[2]:


user = pd.read_csv('user.csv')
user.head()


# In[3]:


tip = pd.read_csv('tip.csv')
tip.head()


# In[4]:


ice = pd.read_csv('ice.csv')
ice.head()


# In[5]:


len(ice)


# In[6]:


review = pd.read_csv('review.csv')
review.head()


# In[10]:


str2 = 'topping, cookie, waffle, crunch, sugar, diary, homemade, custard, price, cheap, expensive, quality, wait, employee, manager, texture, fan, vanilla, chocolate, strawberry, peanut, oreo, caramel, delicious, friendly, small, little, big, fresh, creamy, hard, park, located, location'
str2 = str2.split(', ')


# In[11]:


all_word = review.copy()
for i in str2:
    a=review.text.str.contains(i).apply(lambda x: 1 if x is True else 0)
    all_word[i]=a


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

# In[181]:

# subcategaries of words
flavor = 'vanilla,chocolate,strawberry,peanut,oreo,caramel,custard,waffle,cookie,sugar,creamy'
properties = 'homemade,crunch,quality,texture,small,big,fresh,delicious'
service =  'location,park,friendly,fan,employee,manager,wait,price,expensive'


# In[182]:


flavor = flavor.split(',')
properties = properties.split(',')
service = service.split(',')


# In[14]:


all_word = review.copy()
for i in str2:
    a=review.text.str.contains(i).apply(lambda x: 1 if x is True else 0)
    all_word[i]=a


# In[15]:


all_count = all_word.loc[:,str2].groupby(all_word.stars).sum()


# In[16]:


all_count['small'] += all_count['little']
all_count['location'] += all_count['located']


# In[17]:


all_count.drop(['little','located','diary'], axis = 1, inplace=True)



# In[26]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[79]:

# A trial of chisq test
for i in range(31):
    print(stats.chisquare(all_count.iloc[:,i],prop1*( 5te4s2wall_count.iloc[:,i].sum())))


# In[24]:


all_count


# ## City

# In[29]:


all_ice =  pd.merge(review, ice,how='left',on='business_id')


# In[30]:


all_word1=all_ice.copy()
for i in str2:
    a=review.text.str.contains(i).apply(lambda x: 1 if x is True else 0)
    all_word1[i]=a


# In[70]:

## Binarize the star to make it clear
high = all_word1['stars_x'].isin([4,5]).apply(lambda x: 'high_rating_number' if x is True else 'low_rating_number')


# In[71]:


all_city_hl = all_word1.loc[:,str2].groupby([all_word1['city'],high],sort='false').sum()


# In[72]:


all_city = all_word1.loc[:,str2].groupby([all_word1['city'],all_word1['stars_x']],sort='false').sum()


# ## City of flavor

# In[110]:


high_city={}
for i in all_ice.city.unique():
    high_city[i] = all_city_hl.loc[i,:].loc['high_rating_number',flavor]


# ## Rador plot

# In[229]:


all_ice.city.unique()


# In[225]:


labels=np.array(flavor)
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)# Set the angle
# close the plot

angles=np.concatenate((angles,[angles[0]]))


# In[262]:


stats= high_city[all_ice.city.unique()[0]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2)  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25)  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference - Pittsburgh',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Pitts.png',dpi = 500)


# In[260]:


stats= high_city[all_ice.city.unique()[1]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color = 'r')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25, color='r')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference - Phoenix',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Phoenix.png',dpi = 500)


# In[261]:


stats= high_city[all_ice.city.unique()[2]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='g')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='g')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference - Charlotte',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Char.png',dpi = 500)


# In[263]:


stats= high_city[all_ice.city.unique()[3]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='y')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='y')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference - Las Vegas',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Lasvegas.png',dpi = 500)


# In[264]:


stats= high_city[all_ice.city.unique()[4]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='violet')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='violet')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference - Cleveland',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Cle.png',dpi = 500)


# In[265]:


stats= high_city[all_ice.city.unique()[6]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='black')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='black')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference - Madison',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Madison.png',dpi = 500)


# In[266]:


stats= high_city[all_ice.city.unique()[5]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='orange')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='orange')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Flavor Perference -Champagne',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Flavor/flavor_Cham.png',dpi = 500)


# In[158]:


dict(high_city['Phoenix'])


# In[328]:


df


# In[329]:


import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
# Make a rador map together
df = pd.DataFrame({
'group': all_ice.city.unique(),
})
df.set_axis(df['group'],inplace=True)
for flavor1 in flavor:
    df[flavor1] = np.array([0]*7)
for city in all_ice.city.unique():
    df.loc[city,flavor] = dict(high_city[city]/(high_city[city].sum()))
df.loc['Pittsburgh',flavor] = dict(high_city['Pittsburgh']/(high_city['Pittsburgh'].sum()))
 
# ------- PART 1: Create background
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([])
 


values=df.loc['Pittsburgh'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label='Pittsburgh')
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
values=df.loc['Phoenix'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Phoenix")
ax.fill(angles, values, 'r', alpha=0.1)
 
# Ind2
values=df.loc['Las Vegas'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Las Vegas")
ax.fill(angles, values, 'y', alpha=0.1)

# Ind2
values=df.loc['Charlotte'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Charlotte")
ax.fill(angles, values, 'g', alpha=0.1)

# Ind2
values=df.loc['Madison'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Madison")
ax.fill(angles, values, 'v', alpha=0.1)

# Ind2
values=df.loc['Cleveland'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Cleveland")
ax.fill(angles, values, 'purple', alpha=0.1)

values=df.loc['Urbana'].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Urbana")
ax.fill(angles, values, 'orange', alpha=0.1)
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title('')

plt.savefig('graph-review/Flavor/together.png',dpi = 500)


# ## Service

# In[330]:

high_cityser={}
for i in all_ice.city.unique():
    high_cityser[i] = all_city_hl.loc[i,:].loc['low_rating_number',service]


# In[331]:


labels=np.array(service)
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)# Set the angle
# close the plot

angles=np.concatenate((angles,[angles[0]]))


# In[332]:


stats= high_cityser[all_ice.city.unique()[0]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2)  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25)  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('unsatisfactory service - Pittsburgh',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Service/Serv_Pitts.png',dpi = 500)


# In[333]:


stats= high_cityser[all_ice.city.unique()[1]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color = 'r')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25, color='r')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Unsatisfactory service - Phoenix',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Service/service_Phoenix.png',dpi = 500)


# In[334]:


stats= high_cityser[all_ice.city.unique()[2]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='g')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='g')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Unsatisfactory service - Charlotte',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Service/service_Char.png',dpi = 500)


# In[335]:


stats= high_cityser[all_ice.city.unique()[3]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='y')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='y')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Unsatisfactory service - Las Vegas',y=1.2)
plt.savefig('graph-review/Service/service_Lasvegas.png',dpi = 500)


# In[336]:


stats= high_cityser[all_ice.city.unique()[4]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='violet')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='violet')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Unsatisfactory service - Cleveland',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Service/service_Cle.png',dpi = 500)


# In[339]:


stats= high_cityser[all_ice.city.unique()[6]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='black')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='black')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Unsatisfactory service - Madison',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Service/service_Madison.png',dpi = 500)


# In[338]:


stats= high_cityser[all_ice.city.unique()[5]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='orange')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='orange')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Unsatisfactory service - Madison',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Service/service_Madison.png',dpi = 500)


# # Property
# 

# In[340]:


high_cityser={}
for i in all_ice.city.unique():
    high_cityser[i] = all_city_hl.loc[i,:].loc['low_rating_number',properties]


# In[341]:


labels=np.array(properties)
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)# Set the angle
# close the plot

angles=np.concatenate((angles,[angles[0]]))


# In[309]:


stats= high_cityser[all_ice.city.unique()[0]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2)  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25)  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issues - Pittsburgh',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Property/prop_Pitts.png',dpi = 500)


# In[310]:


stats= high_cityser[all_ice.city.unique()[1]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color = 'r')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25, color='r')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issues - Phoenix',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Property/prop_Phoenix.png',dpi = 500)


# In[311]:


stats= high_cityser[all_ice.city.unique()[2]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='g')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='g')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issues - Charlotte',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Property/prop_Char.png',dpi = 500)


# In[313]:


stats= high_cityser[all_ice.city.unique()[3]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='y')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='y')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issue - Las Vegas',y=1.2)
plt.savefig('graph-review/Property/prop_Lasvegas.png',dpi = 500)


# In[314]:


stats= high_cityser[all_ice.city.unique()[4]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='violet')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='violet')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issue - Cleveland',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Property/prop_Cle.png',dpi = 500)


# In[344]:


stats= high_cityser[all_ice.city.unique()[6]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='black')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='black')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issue - Madison',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Property/prop_Madison.png',dpi = 500)


# In[342]:


stats= high_cityser[all_ice.city.unique()[6]]
stats=np.concatenate((stats,[stats[0]]))  # Closed
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)   # Set polar axis
ax.plot(angles, stats, 'o-', linewidth=2,color='orange')  # Draw the plot (or the frame on the radar chart)
ax.fill(angles, stats, alpha=0.25,color='orange')  #Fulfill the area
ax.set_thetagrids(angles * 180/np.pi, labels) 
ax.set_yticks([])# Set the label for each axis  # Set the pokemon's name as the title
ax.set_title('Other important issue - Madison',y=1.2)
#ax.set_rlim(0,250)
plt.savefig('graph-review/Property/prop_Madison.png',dpi = 500)


