import branca
import folium
import folium.plugins
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import re
import numpy as np
import numpy as np
from datetime import datetime 
import altair as alt
import json
import requests
import pandas as pd
import numpy as np
from folium.plugins import MarkerCluster
from folium.plugins import TimeSliderChoropleth
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import geojson
import geopandas
import shapely
from pandas_geojson import to_geojson
import folium
from folium.features import DivIcon
from folium.plugins import MarkerCluster
from branca.element import Figure
from branca.colormap import linear
import folium
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

style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}




us_counties = (
    "C:/Users/amcfa/Downloads/California_County_Boundaries.geojson"
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
NIL = folium.features.GeoJson(
    us_counties,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME' ],
        aliases = ["County Name "], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(fig2)


color_scale.caption = "Number of stations per county"
color_scale.add_to(fig2)
st.cache(fig2)



###
color_scale1 = LinearColormap(['green','blue'], vmin = min(map1914_dict.values()), vmax = max(map1914_dict.values()))

def get_color(feature):
    value = map1914_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scale1(value)

    
fig3 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)


folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_color(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(fig3)
NIL = folium.features.GeoJson(
    us_counties,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME' ],  # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(fig3)

color_scale1.caption = "Number of stations per county"
color_scale1.add_to(fig3)
st.cache(fig3)



dicts = {"1903-1913":fig2,"1914-1923":fig3,}
years = st.sidebar.selectbox("Please pick a year range",
                             ("1903-1913","1914-1923",))

if years =="1903-1913":
     st_data = st_folium(fig2, width=500)
if years =="1914-1923":
    st_data = st_folium(fig3, width=500)
