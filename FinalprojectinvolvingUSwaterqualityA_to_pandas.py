#%%
## Goals: To compare different areas and contaminant levels, illustrate areas, contaminant levels over time. 
import pandas as pd
import folium
import re



#make sure to install ipyleaflet
#https://catalog.data.gov/dataset/water-quality-data-0de37
pd.set_option('display.max_columns', None)

field_results = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\field_results.csv", low_memory=False)
period_of_record = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\period_of_record.csv",low_memory=False)
stations =pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\stations.csv",low_memory=False)
lab_results = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\lab_results.csv",low_memory=False)

a = lab_results[['latitude','longitude','station_number','sample_date','parameter','result','reporting_limit', 'units']]
b = stations[['latitude','longitude', 'station_number']]
c = field_results[['latitude','longitude','station_number','full_station_name','sample_date','parameter','fdr_result', 'fdr_reporting_limit','uns_name']]
d = period_of_record[['latitude','longitude','station_number','sample_date_max','sample_date_min']]



# %%

a = a.replace('"', '')
b = b.replace('"', '')
c = c.replace('"', '')
c = d.replace('"', '')

#%%
#%%
p = a['sample_date'] = pd.to_datetime(a['sample_date'])
q = a['new_date'] = a['sample_date'].dt.date
# %%
q
#%%
lab_results
stations
period_of_record
# %%
period_of_record

# %%
lab_results

# %%
stations

# %%
stations.sample(n=10)
# %%
stations.describe()
# %%
## Results grouped by area sounds like a good place to start maaybe results limits, lat/long

a = lab_results.select([pl.col('latitude'), pl.col('longitude'),pl.col('station_number'),pl.col('sample_date'),pl.col('parameter'),pl.col('result'), pl.col('reporting_limit'), pl.col('units')])

# %%
b = stations.select([pl.col('latitude'), pl.col('longitude'), pl.col('station_number')])
# %%
c = field_results.select([pl.col('latitude'),pl.col('longitude'),pl.col('station_number'),pl.col('full_station_name'),pl.col('sample_date'),pl.col('parameter'),pl.col('fdr_result'), pl.col('fdr_reporting_limit'),	pl.col('uns_name')])

# %%


# %%
d = period_of_record.select([pl.col('latitude'),pl.col('longitude'),pl.col('station_number'),pl.col('sample_date_max'),pl.col('sample_date_min')])
# %%
##
# %%
a
# %%
b
# %%
c
# %%
d
# %%
m = folium.Map(location = [39.272938,-121.16])
m
# %%
# Here is where I would use some code to iterate over my dfs and merge the data onto the map
#%%
# So this just kinda made a mess, it just looks  
(a.select([
    
	"latitude",
    "longitude",
    "parameter",
    pl.col("parameter").sort_by("latitude").alias("parameters_sorted"),
    pl.col("parameter").sort_by("longitude").alias("parameters_sorted_long"),
]))

# %%
# looks like I need to start earlier in the data. By merging the data frames first. 
# %%
(a.select([
    
	"station_number",
    "sample_date",
    "parameter",
    pl.col("parameter").sort_by("station_number").alias("parameters_sorted"),
    pl.col("parameter").sort_by("station_number").alias("parameters_sorted_long"),
]))
# %%

# %%
pattern = r""
re.split(,)