#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install randomuser')


# In[2]:


from randomuser import RandomUser
import pandas as pd


# In[3]:


r = RandomUser()


# In[4]:


some_list = r.generate_users(10)
some_list


# In[5]:


name = r.get_full_name()


# In[6]:


for user in some_list:
    print (user.get_full_name()," ",user.get_email())


# In[22]:


#To generate a table with information about the users, we can write a function containing all desirable parameters.
#For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed.
#We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return  pd.DataFrame(users) 


# In[23]:


get_users()


# In[10]:


df1 = pd.DataFrame(get_users())  


# In[39]:


def get_u ():
    usres=[]
    r=RandomUser()
    for user in r.generate_users(5):
        usres.append({"name":user.get_full_name(),"phone":user.get_phone(),"state":user.get_state(),"city":user.get_city(),"gender":user.get_gender()})
    return pd.DataFrame(usres)


# In[40]:


get_u()


# In[41]:


#Fruitvice API
import requests
import json


# In[51]:


#We will obtain the fruitvice API data using requests.get("url") function. The data is in a json format.
data = requests.get("https://www.fruityvice.com/api/fruit/all")


# In[52]:


#We will retrieve results using json.loads() function.
results = json.loads(data.text)


# In[53]:


#We will convert our json data into pandas data frame.
pd.DataFrame(results)


# In[54]:


#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
df2


# In[ ]:





# In[ ]:




