#!/usr/bin/env python
# coding: utf-8

# In[758]:


import pandas as pd
from datetime import timedelta, date
import matplotlib.pyplot as plt
import seaborn as sns


# In[759]:


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


# In[760]:


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
df = pd.read_csv(url)


# In[761]:


df = df.drop(columns = ['Province/State', 'Lat', 'Long'])


# In[762]:


countries = ['Italy', 'France', 'Germany', 'US', 'China', 'Russia']
df = df.loc[df['Country/Region'].isin(countries)]   


# In[763]:


start_dt = date(2020, 1, 22)
end_dt = date.today()- timedelta(1)


# In[764]:


for dt in daterange(start_dt, end_dt):
    df[dt.strftime("%-m/%-d/%y")+' sum'] =     df[dt.strftime("%-m/%-d/%y")].groupby(df['Country/Region']).transform('sum')
    df = df.drop(columns = dt.strftime("%-m/%-d/%y"))
# df = df.drop(columns = '1/22/20')
df = df.drop_duplicates()
df.columns = df.columns.str.replace(" sum", "")


# In[765]:


diff = []
for dt in daterange(start_dt, end_dt):
    diff.append(df[dt.strftime("%-m/%-d/%y")])
diff  = pd.DataFrame(diff).T
diff = pd.concat([df['Country/Region'], diff], axis=1)
diff = diff.T
diff.columns = diff.iloc[0]
diff = diff.drop(diff.index[0])
diff


# In[766]:


diff_1 = diff.diff()
diff_1
diff_2 = diff_1.diff()
diff_2


# In[773]:


sns.set(rc={'figure.figsize':(10, 5)})


# In[776]:


diff7_1 = diff.diff(periods=7)
diff7_1
diff7_2 = diff7_1.diff(periods=7)
diff7_2
csv_name = "COVID_2nd_derivative.csv"
diff7_2.to_csv('/Users/mminakova/Documents/COVID/covid_tracker/covid/'+csv_name)


# In[777]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff7_2[cols_plot].plot(marker='.', alpha=0.5, linestyle='-',linewidth = 1, figsize=(40, 10), subplots=True)
# for ax in axes:
#     ax.set_ylabel('Acc.& Dec. of 7 Day New Cases')
axes.legend(fontsize = 'small')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/Acceleration & Deceleration of 7 Day New Cases separately.png')


# In[778]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff7_2[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', figsize=(10, 5), linewidth = 5)

axes.set_ylabel('Acceleration and Deceleration of 7 Day New Cases', fontsize = 10)
axes.legend(fontsize = 'medium')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/Acceleration and Deceleration of 7 Day New Cases all.png')


# In[779]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 5, figsize=(10, 5))

axes.set_ylabel('Total number of confirmed cases', fontsize = 15)
axes.legend(fontsize = 'medium')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/Total number of confirmed cases.png')


# In[780]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff7_1[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 5, figsize=(10, 5))

axes.set_ylabel('7 Day New Cases', fontsize = 15)
axes.legend(fontsize = 'medium')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/7 Day New Cases.png')


# In[ ]:




