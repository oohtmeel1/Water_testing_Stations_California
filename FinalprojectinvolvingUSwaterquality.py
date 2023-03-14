#%%
import pandas as pd
import numpy as np
import polars as pl
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
lab_results.select([pl.col('latitude'), pl.col('longitude'), pl.col('result'), pl.col('reporting_limit'), pl.col('units')])

# %%
stations.select([pl.col('latitude'), pl.col('longitude'), pl.col('station_number'),pl.col('sample_count')])
# %%
