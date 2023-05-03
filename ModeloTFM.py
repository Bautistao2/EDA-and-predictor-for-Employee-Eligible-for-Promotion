#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importo algunas librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets


# In[2]:


#Importo mi dataset [hrdatatrain]
df = pd.read_csv("hrdatatrain.csv")
df.head()


# In[3]:


#dimension  de mi dataset
df.shape


# In[4]:


#Datos estadisticos para algunas de mis columnas
df.describe()


# In[5]:


#Quiero saber si hace falta algun valor para alguna columna
df.info()


# In[6]:


df.is_promoted.value_counts()


# In[7]:


df.isnull().sum()


# In[8]:


df.education.value_counts()


# In[9]:


df.education = df.education.fillna("Bachelor's")


# In[10]:


print(df.education.fillna("Bachelor's"))


# In[11]:


df.education.value_counts()


# In[12]:


df.education.isnull().sum()


# In[13]:


df.education = df.education.replace({"Master's & above": "Master"})


# In[14]:


df.education.isnull().sum()


# In[15]:


df.education.value_counts()


# In[16]:


df.previous_year_rating.value_counts()


# In[17]:


df.previous_year_rating = df.previous_year_rating.fillna(3.0)


# In[18]:


df.previous_year_rating.value_counts()


# In[19]:


df.previous_year_rating.isnull().sum()


# In[20]:


df.department = df.department.map({'Analytics': 0, 'Finance': 1, 'HR': 2, 'Legal': 3,'Operations': 4,'Procurement': 5,'R&D': 6,'Sales & Marketing': 7, 'Technology': 8 })
df.region = df.region.map({'region_1': 1, 'region_2': 2, 'region_3': 3, 'region_4': 4,'region_5': 5,'region_6': 6,'region_7': 7,'region_8': 8, 'region_9': 9,'region_10': 10,'region_11': 11,'region_12': 12, 'region_13' :13,'region_14': 14, 'region_15': 15, 'region_16': 16, 'region_17': 17,'region_18': 18,'region_19': 19,'region_20': 20,'region_21': 21, 'region_22': 22,'region_23': 23,'region_24': 24,'region_25': 25, 'region_26': 26, 'region_27': 27,'region_28': 28,'region_29': 29,'region_30': 30, 'region_31': 31,'region_32': 32,'region_33': 33,'region_34': 34 })
df.education = df.education.map({"Bachelor's": 0,'Below Secondary': 1, 'Master': 2})
df.gender = df.gender.map({"f": 0, 'm': 1})
df.recruitment_channel = df.recruitment_channel.map({"other": 0, 'referred': 1,"sourcing":2 })                                 
  
  
df.head()


# In[21]:


X = df.drop(["employee_id", "is_promoted"], axis = 1)
X.head()


# In[22]:


y = df["is_promoted"]
y.head()


# # ENTRENAMIENTO Y PRUEBA

# In[23]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In[24]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[25]:


len(X_train), len(X_test), len(X)


# In[26]:


(len(X_train)/len(X))*100


# In[27]:


#evaluo diferentes modelos de clasificacion

dtc_model = DecisionTreeClassifier()
log_model = LogisticRegression(max_iter=10000)
rfc_model = RandomForestClassifier()
gsn_model = GaussianNB()
svc_model = SVC()
dtc_model.fit(X_train, y_train)
rfc_model.fit(X_train, y_train)
gsn_model.fit(X_train, y_train)
svc_model.fit(X_train, y_train)
log_model.fit(X_train, y_train)



# In[28]:


print(f"DecisionTreeClassifier: {dtc_model.score(X_test, y_test)}")
print(f"RandomForestClassifier: {rfc_model.score(X_test, y_test)}")
print(f"GaussianNB: {gsn_model.score(X_test, y_test)}")
print(f"SVC: {svc_model.score(X_test, y_test)}")
print(f"logistic : {log_model.score(X_test, y_test)}")


# ##ENTRENO MI MODELO

# In[29]:


import pickle

pickle.dump(rfc_model, open('modelohr.pkl', 'wb'))


# In[30]:


pickled_model = pickle.load(open('modelohr.pkl', 'rb'))
pickled_model.predict([[7, 7, 0, 0, 2, 1, 35, 5, 3, 1, 0, 50]])


# In[ ]:




