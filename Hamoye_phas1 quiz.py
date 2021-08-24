#!/usr/bin/env python
# coding: utf-8

# In[1]:


A=[1,2,3,4,5,6]
B=[13,21,34]
A.extend(B)
A


# In[2]:


np.identity(3)


# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


url='https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
fuel_data = pd.read_csv(url, error_bad_lines=False)
fuel_data.describe()


# In[ ]:


fuel_data.head(5)


# In[ ]:


fuel_data['fuel_mmbtu_per_unit'].describe()


# In[ ]:


fuel_data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].count()


# In[ ]:


graph= sns.barplot(data=fuel_data,x='fuel_type_code_pudl',y='fuel_cost_per_unit_burned')
graph.set_yscale("log")
graph.set_ylim(1, 12000)
plt.xlabel('Fuel Type Code')
plt.ylabel('Fuel Cost per unit Burned')


# In[ ]:


fuel_data.isnull().sum()


# In[ ]:


total_records = fuel_data['record_id'].count()
missing_perc= round(180*100/total_records,3)


# In[ ]:


missing_details={'Feature':'fuel_unit','Total':'180','Percentage': missing_perc}
print(missing_details)


# In[ ]:


graph2 = sns.barplot(data=fuel_data,x='report_year',y='fuel_cost_per_unit_delivered')
graph2.set_yscale('log')
plt.xticks(rotation=90)
plt.xlabel('Report Year')
plt.ylabel('Fuel Cost per unit delivered')


# In[ ]:


fuel_data.groupby('report_year')['fuel_cost_per_unit_burned'].sum()


# In[ ]:




