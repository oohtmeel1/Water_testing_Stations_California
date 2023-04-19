import folium
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
from branca.colormap import LinearColormap
import json

st.header('Visualization of California water testing Data over the last 100 years')

st.image('number_of_testing_stations_over_100_years.png')

st.header('Visualization of California water testing Data over the last 100 years')

st.image('Number of types of tests over the last 100 years.png')




df_grouped1903=pd.read_csv(r"df_grouped1903",index_col=False)
df_grouped1914=pd.read_csv(r"df_grouped1914",index_col=False)
df_grouped1924=pd.read_csv(r"df_grouped1924",index_col=False)
df_grouped1934=pd.read_csv(r"df_grouped1934",index_col=False)
df_grouped1944=pd.read_csv(r"df_grouped1944",index_col=False)
df_grouped1954=pd.read_csv(r"df_grouped1954",index_col=False)
df_grouped1964=pd.read_csv(r"df_grouped1964",index_col=False)
df_grouped1974=pd.read_csv(r"df_grouped1974",index_col=False)
df_grouped1984=pd.read_csv(r"df_grouped1984",index_col=False)
df_grouped1994=pd.read_csv(r"df_grouped1994",index_col=False)
df_grouped2004=pd.read_csv(r"df_grouped2004",index_col=False)
df_grouped2014=pd.read_csv(r"df_grouped2014",index_col=False)
map1903_dict =df_grouped1903.set_index("COUNTY_NAME")["counts"].to_dict()
map1914_dict =df_grouped1914.set_index("COUNTY_NAME")["counts"].to_dict()
map1924_dict =df_grouped1924.set_index("COUNTY_NAME")["counts"].to_dict()
map1934_dict =df_grouped1934.set_index("COUNTY_NAME")["counts"].to_dict()
map1944_dict =df_grouped1944.set_index("COUNTY_NAME")["counts"].to_dict()
map1954_dict =df_grouped1954.set_index("COUNTY_NAME")["counts"].to_dict()
map1964_dict =df_grouped1964.set_index("COUNTY_NAME")["counts"].to_dict()
map1974_dict =df_grouped1974.set_index("COUNTY_NAME")["counts"].to_dict()
map1984_dict =df_grouped1984.set_index("COUNTY_NAME")["counts"].to_dict()
map1994_dict =df_grouped1994.set_index("COUNTY_NAME")["counts"].to_dict()
map2004_dict =df_grouped2004.set_index("COUNTY_NAME")["counts"].to_dict()
map2014_dict =df_grouped2014.set_index("COUNTY_NAME")["counts"].to_dict()





us_counties = (
    "https://github.com/oohtmeel1/ColoradoBoulderVisalizations/blob/main/California_County_Boundaries.json"
)

color_scale = LinearColormap(['green','blue'], vmin = min(map1903_dict.values()), vmax = max(map1903_dict.values()))

def get_color(feature):
    value = map1903_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scale(value)

    
fig2 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)


folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_color(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(fig2)
st.cache(fig2)



dicts = {"1903-1913":fig2,}
years = st.sidebar.selectbox("Please pick a year range",
                             ("1903-1913",))

if years =="1903-1913":
     st_data = st_folium(fig2, width=500)
