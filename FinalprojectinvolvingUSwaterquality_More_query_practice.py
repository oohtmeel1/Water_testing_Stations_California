#%%
## Goals: To compare different areas and contaminant levels, illustrate areas, contaminant levels over time.
# compare number of tests year to year
# Maany metrics 

## To start a good thing would be the number of stations from year to year and the number of tests

import pandas as pd
import folium
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
from matplotlib.text import OffsetFrom
import matplotlib.pyplot as plt
from datetime import datetime 
#%%
# My data set is not supposed to be super huge but you know what. I will use a tiny bit for my project
#https://catalog.data.gov/dataset/water-quality-data-0de37


field_results = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\field_results.csv", low_memory=False)
period_of_record = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\period_of_record.csv",low_memory=False)
stations =pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\stations.csv",low_memory=False)
lab_results = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\lab_results.csv",low_memory=False)



a = lab_results[['latitude','longitude','station_number','sample_date','parameter','result','reporting_limit', 'units']]
b = stations[['latitude','longitude', 'station_number']]
c = field_results[['latitude','longitude','station_number','full_station_name','sample_date','parameter','fdr_result', 'fdr_reporting_limit','uns_name']]
d = period_of_record[['latitude','longitude','station_number','sample_date_max','sample_date_min']]


#%%

#%%
# Replacing all "" with ''

b = b.replace('"', '')
c = c.replace('"', '')
d = d.replace('"', '')

#%%
# Drop all 0 values

#%%

#%%
## So this seemed to work actually to change the Dtype to datetime64
e = a.dtypes['sample_date'] = pd.to_datetime(a['sample_date'])
f = a.assign(sample_date=e)
#%% 
## Finally date time 64. Oh my gosh 
f.dtypes
#%%
f
# %% 
# Drop all 0 values for this new column 
def filter_rows_by_values(df, col, values):
    return f[~f[col].isin(values)]
f = filter_rows_by_values(f,"result",[0])
#%%
f.dtypes

## Now all 0 values are gone 

#%%
## Now this actually works to query the dates and to make the data less overwhelming I will just stick to the last year
g = f[(f['sample_date'] > '2022') & (f['sample_date'] <= '2023')]
#%%
g
#%%

## and now we have unique stations for this year, 180 total
len(g.station_number.unique())
#%% 
## Going to try to use station names and the squeeze method in order to obtain unique station names
## Maybe interesting data would be how many station names there have been over time?
#%%
## So now that how many unique stations were sample in a calendar year 
# I can look at some data.
## How many unique tests were done
len(g.parameter.unique())

## so there were a specific number of tests

# %%
h = f[(f['sample_date'] > '2021') & (f['sample_date'] <= '2022')]
#%%
h
# %%
len(h.station_number.unique())
# %%
len(h.parameter.unique())
# %%
# %%
i = f[(f['sample_date'] > '2020-01-01') & (f['sample_date'] <= '2021-01-01')]
#%%
i
# %%
len(i.station_number.unique())
# %%
len(i.parameter.unique())
# %%
#####################################################
#%%
j = f[(f['sample_date'] > '2019-01-01') & (f['sample_date'] <= '2020-01-01')]
#%%
j
# %%
len(j.station_number.unique())
# %%
len(j.parameter.unique())
# %%
k = f[(f['sample_date'] > '2018-01-01') & (f['sample_date'] <= '2019-01-01')]
#%%
k
# %%
len(k.station_number.unique())
# %%
len(k.parameter.unique())
# %%
l = f[(f['sample_date'] > '2017') & (f['sample_date'] <= '2018')]
#%%
l
# %%
len(l.station_number.unique())
# %%
len(l.parameter.unique())
# %%
m = f[(f['sample_date'] > '2016') & (f['sample_date'] <= '2017')]
#%%
m
# %%
len(m.station_number.unique())
# %%
len(m.parameter.unique())
# %%
# %%
n = f[(f['sample_date'] > '2015') & (f['sample_date'] <= '2016')]
#%%
n
# %%
len(n.station_number.unique())

# %%
len(n.parameter.unique())
# %%

# %%
y = ((len(i.parameter.unique()),len(j.parameter.unique()),len(k.parameter.unique()),len(l.parameter.unique()),len(m.parameter.unique()),len(n.parameter.unique())))
y
#%%
plt.plot(['2015-2016'],[150],'ro')
plt.show()
# %%
x = ['2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
y = ((len(i.parameter.unique()),len(j.parameter.unique()),len(k.parameter.unique()),len(l.parameter.unique()),len(m.parameter.unique()),len(n.parameter.unique())))
y
# %%
fig1 = plt.plot(x,y,'ro')
fig1.show()
#%%
x2 =['2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021'] 
y2 = ((len(i.station_number.unique()),len(j.station_number.unique()),len(k.station_number.unique()),len(l.station_number.unique()),len(m.station_number.unique()),len(n.station_number.unique())))
# %%
fig1, ax = plt.subplots(1)
ax.plot(x, y, 'bs')
ax.plot(x, y2,'ro')
# %%

#%%
len(f.station_number.unique())
f.dtypes
# %%
## So lets build a space for this data to live
# there are 46,000 Different station numbers that were used during the course of this 56 year or so study
# %%
len(f.station_number.unique())
len(f.station_number.unique())


# %%
start_date = f['sample_date'].min()
end_date = f['sample_date'].max()
# %%
start_date
#%%
end_date


# %%
# so uh make a list of 120 empty spaces for all the years to live because there are just a lot of them
## freq 'A means at the end of the year
years = pd.date_range(start=pd.datetime(1903,1,1), periods=120, freq='Y')

# cool to know
# %%
years
# %%
# %%
m = f[(f['sample_date'] > '2016') & (f['sample_date'] <= '2017')]
# %%

# %%

np.dtype('datetime64[ns]') == np.dtype('<M8[ns]')
# %%

# %%
df = pd.DataFrame(years)
df.rename({0: 'years'}, axis=1, inplace=True)
# %%
df['unique_stations'] = " "
# %%
df['yearly_samples'] = " "
# %%
# %%
## after all that effort. A df with blank columns is made
df
# %%

# %%

# %%
df
lst = ""
counter = 0
step = 0
# %%

            
#%%
a = (f.station_number.unique())
b = (f.sample_date.unique())
c = (n.parameter.unique())
        
abc =  pd.DataFrame(a)

# %%
abc
abc['yearly_samples'] = " "
# %%
# %%
for sample in abc[0]:
    if sample in f['station_number'] and f['sample_date'] not in abc:
        print('sample_date')
        abc['yearly_samples'] = abc['yearly_samples']+f['sample_date']
        abc +1
        f + 1
    else:
        break
        
        
# %%
abc= set(abc)
# %%
sample_dates = set()
for sample in abc:
    if sample in f['station_number']:
        if f['sample_date'] not in sample_dates:
            sample_dates.add(f['sample_date'])
            f = f+1 
# %%
abc
# %%
isinstance(f,pd.DataFrame)
# %%
##Trying to troubleshoot how to iterate over my df still. I dont want to have to go manually year by year.
# %%
for sample in abc:
    if sample in f['station_number']:
        f = f
        print(f)
# %%
k = df['years']
m = f[(f['sample_date'] > k)]
# %%
k
# %%

d = {}
for station in f['station_number']:
    d.add((f.sample_date.unique()))
# %%
ad =(f.groupby(['station_number','sample_date'])['sample_date'].count())
# %%

#%%
abc =  pd.DataFrame(ad)
#%%
abc
# %%
abc.rename({'sample_date': 'samples'}, axis=1, inplace=True)
#%%
abc
# %%


## Maybe for years this will help. Back to the draawing board monday 
# Need to see how I can sort this better it is final project after all
start_index = df[df['datetime']=='20100927'].index[0]
days_to_test = 30

for offset in days_to_test:
    fn(df.iloc[start_index:start_index+offset])
# %%
aa = f[(f['sample_date'] > '1903') & (f['sample_date'] <= '1913')]
ab = f[(f['sample_date'] > '1913') & (f['sample_date'] <= '1923')]
ac = f[(f['sample_date'] > '1923') & (f['sample_date'] <= '1933')]
ad = f[(f['sample_date'] > '1933') & (f['sample_date'] <= '1943')]
ae = f[(f['sample_date'] > '1943') & (f['sample_date'] <= '1953')]
af = f[(f['sample_date'] > '1953') & (f['sample_date'] <= '1963')]
ag = f[(f['sample_date'] > '1963') & (f['sample_date'] <= '1973')]
ah = f[(f['sample_date'] > '1973') & (f['sample_date'] <= '1983')]
ai = f[(f['sample_date'] > '1983') & (f['sample_date'] <= '1993')]
aj = f[(f['sample_date'] > '1993') & (f['sample_date'] <= '2003')]
ak = f[(f['sample_date'] > '2003') & (f['sample_date'] <= '2013')]
al = f[(f['sample_date'] > '2013') & (f['sample_date'] <= '2023')]

# %%
aa
# %%
x = ['1903-1913','1903-1923','1923-1933','1933-1943','1943-1953','1953-1963','1963-1973','1973-1983','1983-1993','1993-2003','2003-2013','2013-2023']
y = ((len(aa.station_number.unique()),len(ab.station_number.unique()),
      len(ac.station_number.unique()),len(ad.station_number.unique()),
      len(ae.station_number.unique()),len(af.station_number.unique()),
      len(ag.station_number.unique()),len(ah.station_number.unique()),
      len(ai.station_number.unique()),len(aj.station_number.unique()),
      len(ak.station_number.unique()),len(al.station_number.unique()),
      ))
y
# %%
plt.plot(x, y, 'bs')
plt.show()
# %%
x = ['1903-1913','1903-1923','1923-1933','1933-1943','1943-1953','1953-1963','1963-1973','1973-1983','1983-1993','1993-2003','2003-2013','2013-2023']
y = ((len(aa.parameter.unique()),len(ab.parameter.unique()),
      len(ac.parameter.unique()),len(ad.parameter.unique()),
      len(ae.parameter.unique()),len(af.parameter.unique()),
      len(ag.parameter.unique()),len(ah.parameter.unique()),
      len(ai.parameter.unique()),len(aj.parameter.unique()),
      len(ak.parameter.unique()),len(al.parameter.unique()),
      ))
y
# %%
plt.plot(x, y, 'bs')
plt.show()
# %%
ag
# %%
ag = f[(f['sample_date'] > '1963') & (f['sample_date'] <= '1973')]
# %%
x2 =['1963'] 
y2 = ((len(i.station_number.unique()),len(j.station_number.unique()),len(k.station_number.unique()),len(l.station_number.unique()),len(m.station_number.unique()),len(n.station_number.unique())))
# %%
g = f[(f['sample_date'] > '1963') & (f['sample_date'] <= '1973')]
# %%
g['sample_date'].count()
# %%
g['result'].plot(x="sample_date", y="result")
# %%
## There were a lot of results in 1960's and it seems in the beginning

# %%
aaa = f[(f['sample_date'] > '1963') & (f['sample_date'] <= '1964')]
aab = f[(f['sample_date'] > '1964') & (f['sample_date'] <= '1965')]
aac = f[(f['sample_date'] > '1965') & (f['sample_date'] <= '1966')]
aad = f[(f['sample_date'] > '1966') & (f['sample_date'] <= '1967')]
# %%
aaa['sample_date'].count()
#%%

## So this is where the really big spike was apperently
aab['sample_date'].count()
# %%
aac['sample_date'].count()
# %%
aad['sample_date'].count()
#%%
aad.info()
# %%
results = [part for _, part in f.groupby(pd.Grouper(freq='1Y'))]
# %%

## looks like you can actually sclice a Df based on years as integers.
f[1963:1967]
# %%
