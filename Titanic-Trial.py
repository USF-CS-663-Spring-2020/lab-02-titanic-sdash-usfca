#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np

titanic = pd.read_csv('train.csv')
titanic.head()


# In[3]:


titanic.info()


# In[9]:


#highest Fare

#titanic['Fare'].max()

#lowest Fare
titanic['Fare'].min()

#Average Fare
#titanic['Fare'].mean()
titanic[['Survived','Fare']]

#Number of passenger survived in Titanic
titanic['Survived'].value_counts()


# In[29]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


plt.plot(titanic['Survived'],titanic['Fare'])
plt.xlabel('Survived')
plt.ylabel('Fare')
plt.title('Survival with respect to Fare')


# In[52]:


import seaborn as sns
sns.barplot(x='Survived',y='Fare',data=titanic)


# In[109]:


plt.scatter(x='Fare',y='Survived',data=titanic,marker='d',color='blue')


# In[98]:


fig = plt.figure()

axes = fig.add_axes([0,0,1,1])
plt.bar(titanic['Survived'],titanic['Fare'],color='pink')
#plt.legend()
plt.xticks(titanic['Survived'])
plt.xlabel('Survivals')
plt.ylabel('Fare for Titanic')
plt.title('Survivals with respect to Fare')
plt.show()


# In[85]:


sns.boxplot(x='Survived',y='Fare',data=titanic)


# In[83]:


sns.lmplot(x='Survived',y='Fare',data=titanic)


# In[ ]:




