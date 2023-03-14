#%%
import pandas as pd
import numpy as np
import polars as pl
import folium
#make sure to install ipyleaflet
#https://catalog.data.gov/dataset/water-quality-data-0de37
pd.set_option('display.max_columns', None)

field_results = pl.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\field_results.csv", low_memory=False)
period_of_record = pl.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\period_of_record.csv",low_memory=False)
stations =pl.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\stations.csv",low_memory=False)
lab_results = pl.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\Water quality data\lab_results.csv",low_memory=False)


# %%
field_results
# %%
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
a = lab_results.select([pl.col('latitude'), pl.col('longitude'),pl.col('station_number'), pl.col('result'), pl.col('reporting_limit'), pl.col('units')])

# %%
b = stations.select([pl.col('latitude'), pl.col('longitude'), pl.col('station_number')])
# %%
c = field_results.select([pl.col('latitude'),pl.col('longitude'),pl.col('full_station_name'),pl.col('parameter'),pl.col('fdr_result'), pl.col('fdr_reporting_limit'),	pl.col('uns_name')])

# %%


# %%
d = period_of_record.select([pl.col('latitude'),pl.col('longitude'),pl.col('sample_date_max'),pl.col('sample_date_min')])
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
