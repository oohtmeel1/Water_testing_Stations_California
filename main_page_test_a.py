import folium
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
from branca.colormap import LinearColormap
import json
import geojson
from pandas_geojson import to_geojson

st.header('Visualization of California water testing Data over the last 100 years')

st.image('number_of_testing_stations_over_100_years.png')

st.header('Visualization of California water testing Data over the last 100 years')

st.image('Number of types of tests over the last 100 years.png')
pa=pd.read_csv(r"pa")
pb=pd.read_csv(r"pb")
pc=pd.read_csv(r"pc")
pe=pd.read_csv(r"pe")
pf=pd.read_csv(r"pf")
pg=pd.read_csv(r"pg")
ph=pd.read_csv(r"ph")
pi=pd.read_csv(r"pi")
pj=pd.read_csv(r"pj")
pk=pd.read_csv(r"pk")
pl=pd.read_csv(r"pl")
pm=pd.read_csv(r"pm")



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





geo_json = to_geojson(df=df_grouped1903, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsona = to_geojson(df=df_grouped1914, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsonb = to_geojson(df=df_grouped1924, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsonc = to_geojson(df=df_grouped1934, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsond = to_geojson(df=df_grouped1944, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsone = to_geojson(df=df_grouped1954, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsonf = to_geojson(df=df_grouped1964, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsong = to_geojson(df=df_grouped1974, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsonh = to_geojson(df=df_grouped1984, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsoni = to_geojson(df=df_grouped1994, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])

geo_jsonj = to_geojson(df=df_grouped2004, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])
geo_jsonk = to_geojson(df=df_grouped2014, lat='latitude', lon='longitude',
                 properties=['COUNTY_NAME','counts'])

us_counties = (
  "https://raw.githubusercontent.com/oohtmeel1/ColoradoBoulderVisalizations/main/California_County_Boundaries.json"
)





style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.0, 
                            'weight': 0.0}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.00, 
                                'weight': 0.0}


color_scale = LinearColormap(['green','blue'], vmin = min(map1903_dict.values()), vmax = max(map1903_dict.values()))

def get_color(feature):
    value = map1903_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scale(value)

    
m = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_color(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m)


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
).add_to(m)
m.add_child(NIL)
FIL = folium.features.GeoJson(
    geo_json,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)


m.add_child(FIL)
m.keep_in_front(FIL)
m.add_child(folium.LayerControl())


color_scale.caption = "Number of stations per county"
color_scale.add_to(m)



####

color_scalea = LinearColormap(['green','blue'], vmin = min(map1914_dict.values()), vmax = max(map1914_dict.values()))

def get_colora(feature):
    value = map1914_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalea(value)

    
m1 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colora(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m1)
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
).add_to(m1)
m1.add_child(NIL)

A = folium.features.GeoJson(
    geo_jsona,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations '], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m1.add_child(A)

m1.add_child(folium.LayerControl())


color_scalea.caption = "Number of stations per county"
color_scalea.add_to(m1)

###
color_scaleb = LinearColormap(['green','blue'], vmin = min(map1924_dict.values()), vmax = max(map1924_dict.values()))

def get_colorb(feature):
    value = map1924_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scaleb(value)

    
m2 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colorb(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m2)
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
).add_to(m2)
m2.add_child(NIL)

B = folium.features.GeoJson(
    geo_jsonb,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations '], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m2.add_child(B)

m2.add_child(folium.LayerControl())


color_scaleb.caption = "Number of stations per county"
color_scaleb.add_to(m2)

###

color_scalec = LinearColormap(['green','blue'], vmin = min(map1934_dict.values()), vmax = max(map1934_dict.values()))

def get_colorc(feature):
    value = map1934_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalec(value)

    
m3 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colorc(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m3)
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
).add_to(m3)
m3.add_child(NIL)

C = folium.features.GeoJson(
    geo_jsonc,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m3.add_child(C)

m3.add_child(folium.LayerControl())


color_scalec.caption = "Number of stations per county"
color_scalec.add_to(m3)

###
color_scaled = LinearColormap(['green','blue'], vmin = min(map1944_dict.values()), vmax = max(map1944_dict.values()))

def get_colord(feature):
    value = map1944_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scaled(value)

    
m4 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colord(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m4)
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
).add_to(m4)
m4.add_child(NIL)

D = folium.features.GeoJson(
    geo_jsond,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m4.add_child(D)

m4.add_child(folium.LayerControl())


color_scaled.caption = "Number of stations per county"
color_scaled.add_to(m4)

###
color_scalee = LinearColormap(['green','blue'], vmin = min(map1954_dict.values()), vmax = max(map1954_dict.values()))

def get_colore(feature):
    value = map1954_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalee(value)

    
m5 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colore(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m5)
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
).add_to(m5)
m5.add_child(NIL)

E = folium.features.GeoJson(
    geo_jsone,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m5.add_child(E)

m5.add_child(folium.LayerControl())


color_scalee.caption = "Number of stations per county"
color_scalee.add_to(m5)

###

color_scalef = LinearColormap(['green','blue'], vmin = min(map1964_dict.values()), vmax = max(map1964_dict.values()))

def get_colorf(feature):
    value = map1964_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalef(value)

    
m6 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colorf(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m6)
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
).add_to(m6)
m6.add_child(NIL)

F = folium.features.GeoJson(
    geo_jsonf,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m6.add_child(E)

m6.add_child(folium.LayerControl())


color_scalef.caption = "Number of stations per county"
color_scalef.add_to(m6)


###
color_scaleg = LinearColormap(['green','blue'], vmin = min(map1974_dict.values()), vmax = max(map1974_dict.values()))

def get_colorg(feature):
    value = map1974_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scaleg(value)

    
m7 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colorg(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m7)
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
).add_to(m7)
m7.add_child(NIL)

G = folium.features.GeoJson(
    geo_jsong,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m7.add_child(F)

m7.add_child(folium.LayerControl())


color_scaleg.caption = "Number of stations per county"
color_scaleg.add_to(m7)

###
color_scaleh = LinearColormap(['green','blue'], vmin = min(map1984_dict.values()), vmax = max(map1984_dict.values()))

def get_colorh(feature):
    value = map1984_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scaleh(value)

    
m8 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colorh(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m8)
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
).add_to(m8)
m8.add_child(NIL)

G = folium.features.GeoJson(
    geo_jsong,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m8.add_child(G)

m8.add_child(folium.LayerControl())


color_scaleh.caption = "Number of stations per county"
color_scaleh.add_to(m8)
##
color_scalei = LinearColormap(['green','blue'], vmin = min(map1994_dict.values()), vmax = max(map1994_dict.values()))

def get_colori(feature):
    value = map1994_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalei(value)

    
m9 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colori(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m9)
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
).add_to(m9)
m9.add_child(NIL)

H = folium.features.GeoJson(
    geo_jsonh,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m9.add_child(H)

m9.add_child(folium.LayerControl())


color_scalei.caption = "Number of stations per county"
color_scalei.add_to(m9)

###
color_scalej = LinearColormap(['green','blue'], vmin = min(map2004_dict.values()), vmax = max(map2004_dict.values()))

def get_colorj(feature):
    value = map2004_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalej(value)

    
m10 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colorj(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m10)
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
).add_to(m10)
m10.add_child(NIL)

I = folium.features.GeoJson(
    geo_jsoni,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m10.add_child(I)

m10.add_child(folium.LayerControl())


color_scalej.caption = "Number of stations per county"
color_scalej.add_to(m10)

###
color_scalek = LinearColormap(['green','blue'], vmin = min(map2014_dict.values()), vmax = max(map2014_dict.values()))

def get_colork(feature):
    value = map2014_dict.get(feature['properties']['COUNTY_NAME'])
    if value is None:
        return '#626262'
    else:
        return color_scalek(value)

    
m11 = folium.Map(location=(38.5816,-120.4944),
                 max_bounds=True, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)

folium.GeoJson(
    data = us_counties,
    style_function = lambda feature: {
        'fillColor': get_colork(feature),
        'fillOpacity': 0.7,
        'color' : 'black',
        'weight' : 1,
    }    
).add_to(m11)
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
).add_to(m11)
m11.add_child(NIL)

J = folium.features.GeoJson(
    geo_jsonj,
    style_function=style_function, 
    control=True,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'
                ,'counts'],
        aliases = ["County Name"
                   ,'number of stations'], # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        
    )
)
m11.add_child(J)

m11.add_child(folium.LayerControl())


color_scalek.caption = "Number of stations per county"
color_scalek.add_to(m11)







dicts = {"1903-1913":m,"1914-1923":m1,"1924-1933":m2,"1934-1943":m3,"1944-1953":m4,"1954-1963":m5,"1964-1973":m6,"1974-1983":m7,"1984-1993":m8,"1994-2003":m9,"2004-2013":m10,"2014-2023":m11}
years = st.sidebar.selectbox("Please pick a year range",
                             ("1903-1913","1914-1923","1924-1933","1934-1943","1944-1953","1954-1963","1964-1973","1974-1983","1984-1993","1994-2003","2004-2013","2014-2023"))

if years =="1903-1913":
    st_data = st_folium(m, width=500)
    st.sidebar.table(data=pa)
if years =="1914-1923":
    st_data = st_folium(m1, width=500)
if years == "1924-1933":
    st_data = st_folium(m2, width=500)
if years == "1934-1943":
    st_data = st_folium(m3, width=500)
if years == "1944-1953":
    st_data = st_folium(m4, width=500)
if years == "1954-1963":
    st_data = st_folium(m5, width=500)
if years == "1964-1973":
    st_data = st_folium(m6, width=500)
if years == "1974-1983":
    st_data = st_folium(m7, width=500)
if years == "1984-1993":
    st_data = st_folium(m8, width=500)
if years == "1994-2003":
    st_data = st_folium(m9, width=500)
if years == "2004-2013":
    st_data = st_folium(m10, width=500)
if years == "2014-2023":
    st_data = st_folium(m11, width=500)

