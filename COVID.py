#!/usr/bin/env python
# coding: utf-8

# In[617]:


import pandas as pd
from datetime import timedelta, date
import matplotlib.pyplot as plt
import seaborn as sns


# In[658]:


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


# In[659]:


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
df = pd.read_csv(url)


# In[660]:


df = df.drop(columns = ['Province/State', 'Lat', 'Long'])


# In[661]:


countries = ['Italy', 'France', 'Germany', 'US', 'China', 'Russia']
df = df.loc[df['Country/Region'].isin(countries)]   


# In[662]:


start_dt = date(2020, 1, 22)
end_dt = date.today()- timedelta(1)


# In[663]:


for dt in daterange(start_dt, end_dt):
    df[dt.strftime("%-m/%-d/%y")+' sum'] =     df[dt.strftime("%-m/%-d/%y")].groupby(df['Country/Region']).transform('sum')
    df = df.drop(columns = dt.strftime("%-m/%-d/%y"))
# df = df.drop(columns = '1/22/20')
df = df.drop_duplicates()
df.columns = df.columns.str.replace(" sum", "")


# In[689]:


diff = []
for dt in daterange(start_dt, end_dt):
    diff.append(df[dt.strftime("%-m/%-d/%y")])
diff  = pd.DataFrame(diff).T
diff = pd.concat([df['Country/Region'], diff], axis=1)
diff = diff.T
diff.columns = diff.iloc[0]
diff = diff.drop(diff.index[0])
diff


# In[690]:


diff_1 = diff.diff()
diff_1
diff_2 = diff_1.diff()
diff_2


# In[719]:


csv_name = "COVID_2nd_derivative.csv"
diff_2.to_csv('/Users/mminakova/Documents/COVID/covid_tracker/covid/'+csv_name)


# In[668]:


sns.set(rc={'figure.figsize':(20, 10)})


# In[692]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff_2[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 1, figsize=(40, 40), subplots=True)
for ax in axes:
    ax.set_ylabel('2nd derivative')
    ax.legend(fontsize = 'xx-large')


# In[693]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff_2[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 5, figsize=(40, 40))

ax.set_ylabel('2nd derivative')
ax.legend(fontsize = 'xx-large')


# In[704]:


diff7_1 = diff.diff(periods=7)
diff7_1
diff7_2 = diff7_1.diff(periods=7)
diff7_2


# In[705]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff7_2[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 1, figsize=(40, 40), subplots=True)
for ax in axes:
    ax.set_ylabel('2nd derivative')
    ax.legend(fontsize = 'xx-large')


# In[711]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff7_2[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 5, figsize=(40, 40))

ax.set_ylabel('2nd derivative')
ax.legend(fontsize = 'xx-large')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/COVID_7_2.png')


# In[712]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 5, figsize=(40, 40))

ax.set_ylabel('2nd derivative')
ax.legend(fontsize = 'xx-large')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/COVID_raw.png')


# In[717]:


cols_plot = ['Germany', 'Italy', 'US', 'China', 'France', 'Russia']
axes = diff7_1[cols_plot].plot(marker='.', alpha=0.5, linestyle='-', linewidth = 5, figsize=(40, 40))

ax.set_ylabel('2nd derivative')
ax.legend(fontsize = 'xx-large')
plt.savefig('/Users/mminakova/Documents/COVID/covid_tracker/covid/COVID_7_1dev.png')


# In[ ]:




