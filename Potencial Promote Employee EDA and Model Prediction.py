#!/usr/bin/env python
# coding: utf-8

# ## Importing Packages

# In[74]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LinearRegression
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from simple_colors import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
from plotnine import *
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.feature_selection import f_classif, chi2, mutual_info_classif
from sklearn.feature_selection import SelectKBest


# ## Load and read data

# In[3]:


# loading the dataset to pandas dataframe
df = pd.read_csv("hrdataappPPE.csv")
df.head()


# In[4]:


df.tail()


# In[5]:


#Dataset Size
df.shape


# In[6]:


print("Dataset has {} data  with {} variables each.".format(*df.shape))


# # Explotory Data Analysis (EDA) & Visualization

# In[7]:


df.reindex()


# In[8]:


# statistical measure of dataset
df.describe()


# In[9]:


#Get information about DataFrame
df.info()


# **Commits**
# *We only have NULL values in "Education" & "previous_year_rating" columns

# In[10]:


#check missing values
df.isnull().sum()


# In[11]:


df.education.value_counts()


# In[12]:


df.education = df.education.fillna("Bachelor's")
df


# In[13]:


df.education.value_counts()


# In[14]:


df.previous_year_rating.value_counts()


# In[15]:


df.previous_year_rating = df.previous_year_rating.fillna(3.0)
df


# In[16]:


df.previous_year_rating.value_counts()


# In[17]:


df.isnull().sum()


# In[18]:


df= df.rename(columns={'employee_id':'Emp_ID', 'department':'Department','region':'No_of_Region','education':'Level_of_education','gender':'Gender','recruitment_channel':'Recruitment_channel','no_of_trainings' :'No_of_other_trainings_completed','age':'Age','previous_year_rating':'Performance_Score', 'length_of_service':'Length_of_service','KPIs_met >80%':'High_KPIS','awards_won?':'Awards_won','avg_training_score':'Average_score_evaluations' })


# In[19]:


df.drop_duplicates(inplace=True)
df


# **Commits**
# *The data types are appropriate.*
# *The dataset covers data on 54808 employees.*
# 

# In[20]:


for column in df.select_dtypes(include='O').columns:
    print(blue(f'{column}', 'bold')) 
    print(black('Number of unique values :', 'underlined'), df[column].nunique())
    if column == 'employee_id':
        print(df[column].unique()[:30])
    else:
        print(df[column].unique())
    print()


# In[21]:


#How many employees have been promoted and not?
df['is_promoted'].value_counts()


# In[22]:


print('1. The percentage of employees who have not received a promotion are ' + str(round((50140/54808)*100,2)) + '%')
print('2. The percentage of employees who get promoted are ' + str(round((4668/54808)*100,2)) + '%')


# **Commits**
# -Dataframe have 14 columns and 54808 rows
# -Total categorical columns are 5 columns
# -Total numerical columns are 9 columns
# -There are 2 columns that have a missing value (education and previous_year_rating)
# -is_promoted column is the target for this dataset
# 

# ## DATA VISUALIZATION

# ### Now, some charts for the most relevant information of the data

# In[23]:


df.is_promoted.value_counts().plot(kind="bar")
plt.xlabel('Promoted employees')
plt.ylabel('Values')
plt.show()


# **Now let's go to go in depth to know parameters of influence in the promotion of employees**

# ### About Employee's gender

# In[24]:


df['Gender']


# In[25]:


df['Gender'].unique()


# In[26]:


opciones = ["Gender"]

for opcion in opciones:
    print('opcion:', opcion, 'con is_promoted ')
    pd.crosstab(df[opcion], df.is_promoted).plot(kind="bar")
    plt.xlabel('Gender')
    plt.ylabel('Values')
    plt.show()


# **More men than women are trained annually, and men are more promoted**

# In[27]:


Genderpro = pd.merge(right=df.groupby(['Gender'])[['Emp_ID']].count().reset_index(), left=df.groupby(['Gender'])[['is_promoted']].sum().reset_index(), on='Gender', how="outer")

Genderpro['AbsRatio'] = round(Genderpro['is_promoted']/Genderpro['Emp_ID'], 2)
Genderpro.sort_values(by=['AbsRatio'], ascending=False, inplace=True)
plt.figure(figsize=(8, 5))
sns.barplot(Genderpro, x='AbsRatio', y='Gender', width=0.7, orient='h')
plt.title("Total promoted employees by gender")
plt.xlabel('Ratio of promoted employees');


# **The number of trained female employees that passes is greater than that of men, this means that from a group of women and men, promotion in women is more effective.**

# In[28]:


df.groupby("Gender").is_promoted.value_counts()


# **Now, I create a dataframe to analyze the workers who have been promoted**

# In[29]:


df_ispromoted = df[df.is_promoted==1]


# In[30]:


df_ispromoted.value_counts()


# In[31]:


df_ispromoted.shape


# In[32]:


opciones1 = ["Gender"]

for opcion in opciones:
    print('Promoteed  ''and:', opcion, )
    pd.crosstab(df_ispromoted[opcion], df.Gender).plot(kind="bar")
    plt.xlabel('Gender')
    plt.ylabel('Values')
    plt.show()


# In[33]:


opciones2 = ["Recruitment_channel"]

for opcion in opciones2:
    print('opcion:', opcion, 'vs is Gender')
    pd.crosstab(df_ispromoted[opcion], df.Gender).plot(kind="bar")
    plt.xlabel('Recruitment Channel')
    plt.ylabel('Values')
    plt.show()


# In[34]:


df.groupby("Recruitment_channel").is_promoted.value_counts()


# In[35]:


print('1. The percentage of employees who have received a promotion and have been employed by referred channel is ' + str(round((138/4668)*100,2)) + '%')
print('2. The percentage of employees who have received a promotion and have been employed by sourcing channel is  ' + str(round((1974/4668)*100,2)) + '%')
print('2. The percentage of employees who have received a promotion and have been employed by other channel is  ' + str(round((2556/4668)*100,2)) + '%')


# **Regarding the recruitment channel, the recruitment channel that contributes the least promotions is the one in which company employees refer their acquaintances, with 3% of the total promotions, on the other hand, using external companies has contributed close to 42% of promoted employees, while other types of recruitment such as internet pages have contributed 55% of the promotions, in conclusion hiring through referrals and external companies should be reduced and the search for candidates through internet pages that present more skills should be increased**

# In[92]:


opciones4 = ['Department','Level_of_education','Recruitment_channel','No_of_other_trainings_completed','Age','Performance_Score','Length_of_service', 'High_KPIS','Awards_won','Average_score_evaluations']

for opcion in opciones4:
    print('opcion:', opcion, 'vs gender')
    pd.crosstab(df_ispromoted[opcion], df.Gender).plot(kind="bar")
    plt.ylabel('Employees')
    plt.show()


# **-Employees who have missed a maximum of two training sessions should be preferred; more than two are not potentially promotable.**
# 
# **-Employees between 26 and 39 are more likely to be promoted than other ages, both men and women.**
# 
# **-Employees with performance scores of 3 and 5 have mostly been promoted, employees with 1, 2 and even 4 are not potentially promotable.**
# 
# **-Employees with less than 8 years of seniority in the company are mostly promoted; the older they are, the lower the employee promotion, with seniority inversely proportional to the number of promotions.**
# 
# **-The number of employees promoted with high KPIS is twice the number of employees promoted without high KPIS, this means that the value of the KPIS measured on the employees directly affects the probability of being promoted.**
# 
# **-It is curious that the same does not happen with employees who have won awards in the company, there are much more promoted employees who have not won any awards than those who have won, this means that it does not represent an advantage when it comes to to promote but on the contrary, employees with awards may feel more relaxed and do not put as much effort into promotion tests.**
# 
# **-An employee with any average score evaluations can be promoted**
# 

# In[37]:


#Plot a histrogram to understand the distribution of the promotee employees by age.

plt.figure(figsize = (15,7))
ax = sns.histplot(df_ispromoted.Age)
for c in ax.containers:
   ax.bar_label(c,label_type = 'edge')
   


# In[38]:


#Understanding the differences in number of promotion by gender by plotting a bell curve. 
Male = df_ispromoted[df_ispromoted['Gender'] == "m"]
Female = df_ispromoted[df_ispromoted['Gender'] == "f"]

ggplot(data = df_ispromoted, mapping = aes(x = 'Age', fill = 'Gender')) +  geom_density()


# **-The age of the company's employees ranges between 20 and 60 years old and although there are promoted employees, employees aged between 25 and 40 are potentially promotable, the number of promoted employees increases from 27 to 35 years old.**

# In[39]:


#Plot a histrogram to understand the distribution of the promotee employees by performance Score.

plt.figure(figsize = (15,7))
ax = sns.histplot(df_ispromoted.Performance_Score)
for c in ax.containers:
   ax.bar_label(c,label_type = 'edge')


# In[40]:


#Understanding the differences in number of promotion by gender by plotting a bell curve. 
Male = df_ispromoted[df_ispromoted['Gender'] == "m"]
Female = df_ispromoted[df_ispromoted['Gender'] == "f"]

ggplot(data = df_ispromoted, mapping = aes(x = 'Performance_Score', fill = 'Gender')) +  geom_density()


# In[41]:


#Plot a histrogram to understand the distribution of the promotee employees by Length of service.

plt.figure(figsize = (15,7))
sns.histplot(data=df_ispromoted,  x="Length_of_service", kde=True)
for c in ax.containers:
   ax.bar_label(c,label_type = 'edge')


# ### About recruitment chanel

# In[42]:


opciones6 = ["Recruitment_channel"]

for opcion in opciones6:
    print('opcion:', opcion, 'vs is_promoted ')
    pd.crosstab(df[opcion], df.is_promoted).plot(kind="bar")
    plt.xlabel('Recruitment_channel')
    plt.ylabel('Values')
    plt.show()


# In[43]:


df_ispromoted.Recruitment_channel.value_counts().plot(kind="bar")
plt.xlabel('Recruitment_channel')
plt.ylabel('Values')
plt.show()


# In[44]:


EmpAbs = pd.merge(right=df.groupby(['Recruitment_channel'])[['Emp_ID']].count().reset_index(), left=df.groupby(['Recruitment_channel'])[['is_promoted']].sum().reset_index(), on='Recruitment_channel', how="outer")

EmpAbs['AbsRatio'] = round(EmpAbs['is_promoted']/EmpAbs['Emp_ID'], 2)
EmpAbs.sort_values(by=['AbsRatio'], ascending=False, inplace=True)
plt.figure(figsize=(8, 5))
sns.barplot(EmpAbs, x='AbsRatio', y='Recruitment_channel', width=0.7, orient='h')
plt.title("Total promoted employees by recruitment channel")
plt.xlabel('Ratio of promoted employees');


# **-In relation to employees who apply for promotion and those who pass, training to be promoted is more effective in workers who have been employed through a referral, over sourcing and other recruitment channel**

# In[45]:


sns.kdeplot(data=df_ispromoted, x="No_of_other_trainings_completed", hue="Recruitment_channel")


# **The trend in the number of past trainings completed in promoted employees remains the same for the three recruitment channels used by the company.**

# In[46]:


sns.kdeplot(data=df_ispromoted, x="Length_of_service", hue="Recruitment_channel")


# **The trend in the length of service in promoted employees remains the same for the three recruitment channels used by the company.**

# In[47]:


sns.kdeplot(
   data=df_ispromoted, x="Performance_Score", hue="Recruitment_channel",
   fill=True, common_norm=False, palette="pastel",
   alpha=.5, linewidth=0,
)


# **The trend in the Performance Score in promoted employees remains the same for the three recruitment channels used by the company.**

# ### About the level of education
# 

# **It is already known that employees with a bachelor's education level have been mostly promoted, now let's see how this characteristic relates to other parameters**

# In[48]:


#Level of education and high KPIS


# In[49]:


opciones4 = ['Recruitment_channel','No_of_other_trainings_completed','Age','Performance_Score','Length_of_service', 'Awards_won','Average_score_evaluations']

for opcion in opciones4:
    print('Level of education'' and:', opcion, )
    pd.crosstab(df_ispromoted[opcion], df.Level_of_education).plot(kind="bar")
    plt.ylabel('Values')
    plt.show()


# **Regarding the level of education of the employees, the vast majority of employees promoted with only 1 and 2 training sessions missed only had a bachelor's degree, and not a master's degree, that is, having a master's degree does not indicate a greater probability of promotion.**

# In[50]:


df


# In[51]:


my_df = df.select_dtypes(exclude=[object])


# In[52]:


plt.figure(figsize=(16, 20))
heatmap = sns.heatmap(my_df.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);


# **From the data matrix it can be concluded that of all the employee features, those that have the most relationship with employee promotion are:**
# 
#    **-Performance score, High KPIS, Awards won and Average score evaluations.**
#     

# ## Build & Training a Machine Learning Algorithm:

# In[53]:


df.info()


# In[54]:


df.Level_of_education = df.Level_of_education.replace({"Master's & above": "Master"})


# In[55]:


#change categorical variables to numerical variables

df.Department = df.Department.map({'Analytics': 0, 'Finance': 1, 'HR': 2, 'Legal': 3,'Operations': 4,'Procurement': 5,'R&D': 6,'Sales & Marketing': 7, 'Technology': 8 })
df.No_of_Region = df.No_of_Region.map({'region_1': 1, 'region_2': 2, 'region_3': 3, 'region_4': 4,'region_5': 5,'region_6': 6,'region_7': 7,'region_8': 8, 'region_9': 9,'region_10': 10,'region_11': 11,'region_12': 12, 'region_13' :13,'region_14': 14, 'region_15': 15, 'region_16': 16, 'region_17': 17,'region_18': 18,'region_19': 19,'region_20': 20,'region_21': 21, 'region_22': 22,'region_23': 23,'region_24': 24,'region_25': 25, 'region_26': 26, 'region_27': 27,'region_28': 28,'region_29': 29,'region_30': 30, 'region_31': 31,'region_32': 32,'region_33': 33,'region_34': 34 })
df.Level_of_education   = df.Level_of_education.map({"Bachelor's": 0,'Below Secondary': 1, 'Master': 2})
df.Gender = df.Gender.map({"f": 0, 'm': 1})
df.Recruitment_channel = df.Recruitment_channel.map({"other": 0, 'referred': 1,"sourcing":2 })                                 
  
  
df.head()


# In[56]:


# drop the 'Emp_ID' column from the DataFrame to create the feature matrix
X = df.drop(["Emp_ID", "is_promoted"], axis = 1)
X.head()


# In[57]:


# create the target vector
y = df["is_promoted"]
y.head()


# In[68]:


# split the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[69]:


# check shape
print('x_train: ', X_train.shape)
print('x_test: ', X_test.shape)
print('y_train: ', y_train.shape)
print('y_test: ', y_test.shape)


# ### Build prediction Models

# In[ ]:


#training Model predictions 
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


# In[71]:


# create a dictionary of models
models = {
    "dtc_model":DecisionTreeClassifier(),
    "log_model": LogisticRegression(),
    "rfc_mode": RandomForestClassifier(),
    "gsn_mode": GaussianNB(),
    "svc_model": SVC(),
   
}

# loop through the models and fit each one to the training data
for name, model in models.items():
    model.fit(X_train, y_train)
    print(name + " trained.")


# In[73]:


# loop through the models and make predictions on the test data
for name, model in models.items():
    print(name + " Accuracy: {:.2f}%".format(model.score(X_test, y_test) * 100))
    y_pred = model.predict(X_test)
    
  # plot the confusion matrix as a heatmap
    cm = confusion_matrix(y_test, y_pred)
    ax = sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    ax.set_title(name + " Confusion Matrix")
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    plt.show()
    
    # print the classification report for each model
    report = classification_report(y_test, y_pred)
    print(name + " Classification Report:")
    print(report)   
    
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


# In[75]:


selector = SelectKBest(k=10, score_func=f_classif)


# In[76]:


selector.fit(X_train, y_train)


# In[77]:


selector.get_support(indices=True)


# In[79]:


df.columns[selector.get_support(indices=True)]


# In[86]:


Select_columns = pd.DataFrame({'Important_Feature':df.columns[selector.get_support(indices=True)],
                  'Score':selector.get_support(indices=True)} )
Select_columns


# In[101]:


plt.figure(figsize=(16,15))
sns.barplot(x='Score', y='Important_Feature', data=Select_columns)
plt.xlabel('Score in the prediction model');
plt.ylabel('Features');
plt.ylabel('Features');
plt.title("Influence of the feautures in the prediction model")


# In[91]:


#export and save my prediction model
import pickle
from array import array

pickle.dump(rfc_model, open('modelpredictionppe.pkl', 'wb'))

