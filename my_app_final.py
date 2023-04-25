# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import folium
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
from branca.colormap import LinearColormap
import json
import geojson
from pandas_geojson import to_geojson
import altair as alt
from PIL import Image


st.set_page_config(layout="wide")
image = Image.open('Deptofwaterresources.jpg')
def main_page():
    st.title("An analysis of California's DWR testing stations")
    st.image(image, caption='Department of water resources logo (Wikipedia)')
    st.header(""" A brief introduction:
                                                  Some of the data comes from the Data.Gov repository, 
        a great free resource. Some came from wikipedia. Some came from California state websites. 
        All of it came together to help create my presentation. 
        Each data set contained hundreds if not thousands of points and I cleaned,sorted, organized
        and visualized it all. 
        For example just the original data set consisted of 4 separate subsets.
        Stations- listing all stations
        Periods of record- Ranges for all times and dates that substations were used for sampling.
        Field results - A list of all testing results that were able to be taken in the field.
        Lab Results- A list of all testing performed in facilities.
        But that data alone needed additional data to give it more weight, more impact. 
        So population data and budgetary data for the state of California was also included.
        Thank you for taking the time to look it over. 
        
""")
    

    st.header("""Goals:
              Clean water is an important and vital resource for everyone.
    The DWR takes samples of drinking water, ground water and other sources. And tests it for safety and 
    quality. Where and how often is this testing taking place? 
    Is there less now in some counties than in others?
    While on the surface this data set seems mundane, in reality it contained a huge amount of depth 
    with mountains of useful information just waiting to be parsed and shared. It was a great data set to get people talking and thinking. 
    My goals for this presentation were to provide information in a way that was clear and hopefully easy to understand. 
    To get people to ask questions and think about what goes on around them.
    I wanted to visualize the numbers of stations over the course of some amount of time. And make comparisons between different counties.
    
              """)
    st.header("""Tasks:
        The tasks that were most important were:
    1) Organizing the data accurately, making sure nothing was missed or left out.
    2) Putting it all together in a way that made sense and looked good.
    3) Providing useful information.
              """)
    st.header("""Data Sources: 
              https://catalog.data.gov/dataset/water-quality-data-0de37
    https://www.counties.org/data-and-research
    https://lao.ca.gov/analysis
    https://law.stanford.edu
    https://en.wikipedia.org/wiki/California_Department_of_Water_Resources
              
              
              """)
    
    

def page2():    

    st.sidebar.markdown("Final Project, please close the sidebar to see this best")


    pa=pd.read_csv(r"pa",index_col=False)
    pb=pd.read_csv(r"pb",index_col=False)
    pc=pd.read_csv(r"pc",index_col=False)
    pe=pd.read_csv(r"pe",index_col=False)
    pf=pd.read_csv(r"pf",index_col=False)
    pg=pd.read_csv(r"pg",index_col=False)
    ph=pd.read_csv(r"ph",index_col=False)
    pi=pd.read_csv(r"pi",index_col=False)
    pj=pd.read_csv(r"pj",index_col=False)
    pk=pd.read_csv(r"pk",index_col=False)
    pl=pd.read_csv(r"pl",index_col=False)
    pm=pd.read_csv(r"pm",index_col=False)
    budget1984percent = pd.read_csv(r'budget1984percent',index_col=False)
    budget1984=pd.read_csv(r"budget1984",index_col=False)
    pool=pd.read_csv(r"1984populationranked",index_col=False)


    budget1994percent = pd.read_csv(r'budget1994percent',index_col=False)
    budget1994=pd.read_csv(r"budget1994",index_col=False)
    poola=pd.read_csv(r"1994populationranked",index_col=False)


    budget2004percent = pd.read_csv(r'budget2004percent',index_col=False)
    budget2004=pd.read_csv(r"budget2004",index_col=False)
    poolb=pd.read_csv(r"2004populationranked",index_col=False)

    budget2023percent = pd.read_csv(r'budget2023percent',index_col=False)
    budget2023=pd.read_csv(r"budget2023",index_col=False)
    poolc=pd.read_csv(r"2023populationranked",index_col=False)


    df_grouped1974=pd.read_csv(r"df_grouped1974",index_col=False)
    df_grouped1984=pd.read_csv(r"df_grouped1984",index_col=False)
    df_grouped1994=pd.read_csv(r"df_grouped1994",index_col=False)
    df_grouped2004=pd.read_csv(r"df_grouped2004",index_col=False)
    df_grouped2014=pd.read_csv(r"df_grouped2014",index_col=False)

    map1974_dict =df_grouped1974.set_index("COUNTY_NAME")["counts"].to_dict()
    map1984_dict =df_grouped1984.set_index("COUNTY_NAME")["counts"].to_dict()
    map1994_dict =df_grouped1994.set_index("COUNTY_NAME")["counts"].to_dict()
    map2004_dict =df_grouped2004.set_index("COUNTY_NAME")["counts"].to_dict()
    map2014_dict =df_grouped2014.set_index("COUNTY_NAME")["counts"].to_dict()







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
    m7.add_child(G)

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
    m8.add_child(H)

    m8.add_child(folium.LayerControl())



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
    m9.add_child(I)

    m9.add_child(folium.LayerControl())




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
    m10.add_child(J)

    m10.add_child(folium.LayerControl())




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

    K = folium.features.GeoJson(
        geo_jsonk,
        style_function=style_function, 
        control=True,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['COUNTY_NAME'
                    ,'counts'],
            labels = False,
            sticky =True,
            markertooltip = False,
            aliases = ["County Name"
                    ,'number of stations'], # use fields from the json file
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
            
        )
    )
    m11.add_child(K)

    m11.add_child(folium.LayerControl())



    image = Image.open('Deptofwaterresources.jpg')



        
    ###########################################  
    # Turn into a DF

    st.title("An analysis of California's DWR testing stations")

    dicts = {"1984-1993":m8,"1994-2003":m9,"2004-2013":m10,"2014-2023":m11}
    years = st.selectbox("Please pick a year range",
                                ("1984-1993","1994-2003","2004-2013","2014-2023"))
    col1,col2,col3 = st.columns([4,4,2])
    if years == "1984-1993":
        with col1:
            st.markdown("""A color map, of the counts of testing stations for the DWR 
                        in California counties. 
                        The tooltips can be hidden by 
                        hovering over the layers icon in the upper right hand of the map.
                        As the counts increase the color deepens, if no stations are counted,
                        the color of the county will display as gray.
                        """)
            st_data = st_folium(m8)
            st.dataframe(data=pj,height=300)                                                                                                                                                       
        with col3:
            st.markdown("""A dataframe of California's budget data, 
                        containing the total state budget (in dollars),
                        how much was alloted to the DWR, 
                        and what % that ended up being. """)
            st.dataframe(budget1984percent,height=280)
            st.markdown("""A dataframe of California's population data. The mean population was calculated.
                        Each population was ranked, 
                        and the number of testing stations was also ranked.""")
            st.dataframe(pool,height=280)
        with col2:
            
            st.markdown("""The Budget of California VS 
                        the amount set aside for the Department of Water Resources.
                        Hovering over the bars reveals tooltips with additional information.""")
            title = alt.TitleParams('Budget of California Vs % used by DWR', anchor = 'middle')
            bar_chart = alt.Chart(budget1984,title=title).mark_bar().encode(
                x="years:O",
                y=alt.Y("state_budget",title ='Budget of California'),
                color =alt.Color('state_budget', scale=alt.Scale(scheme='yellowgreenblue',zero=False),legend=None),
                tooltip=[alt.Tooltip('DWR', title="DWR Budget "),
                        alt.Tooltip("% of budget to DWR", title= '% of budget to DWR')])
            layer = alt.Chart(budget1984).mark_bar().encode(
                x="years:O",
                y="entire_budget:Q",
                tooltip=[alt.Tooltip('state_budget', title="State budget ")]
            )
            
            st.altair_chart(bar_chart+ layer, use_container_width=True)
            st.markdown("""The rankings of the populations
                        of each county as bars and the rankings 
                        of the numbers of stations per county as circles.
                        Note, for population, higher ranking means higher population.
                        And if station count is missing. It was not in the data itself.""")
            title = alt.TitleParams('County population means VS station counts', anchor = 'middle')
            not_bar = alt.Chart(pool,title=title).mark_bar().encode(
                y =alt.Y('County', sort = None),
                x=alt.X("Population_rank",title ='Population rank of county'),
                color =alt.Color('Population_rank', scale=alt.Scale(scheme='blueorange',zero=False),legend= None),
                tooltip=[alt.Tooltip('County', title="Name of County: "),
                        alt.Tooltip('Population', title=" mean population "),
                        alt.Tooltip('Population_rank')])
            layers = alt.Chart(pool).mark_circle().encode(
                y =alt.Y('County', sort = None),
                x="Station rank:Q",
                tooltip=[alt.Tooltip('Station count', title="Station count "),
                        alt.Tooltip("Station rank", title= 'Station rank')])
            
            
            
            st.altair_chart(not_bar+layers,use_container_width=True)
        
            
    # Attempt to use Altair to make it look nicer

            
    if years == "1994-2003":
        with col1:
        
                st.markdown("""A color map, of the counts of testing stations for the DWR 
                        in California counties. 
                        The tooltips can be hidden by 
                        hovering over the layers icon in the upper right hand of the map.
                        As the counts increase the color deepens, if no stations are counted,
                        the color of the county will display as gray.
                        """)
                st_data = st_folium(m9)
                st.dataframe(data=pk,height=300)                                                                                                                                                       
                with col3:
                    st.markdown("""A dataframe of California's budget data, 
                        containing the total state budget (in dollars),
                        how much was alloted to the DWR, 
                        and what % that ended up being. """)
                    st.dataframe(budget1984percent,height=280)
                    st.markdown("""A dataframe of California's population data. The mean population was calculated.
                        Each population was ranked, 
                        and the number of testing stations was also ranked.""")
                    st.dataframe(poola,height=280)
                    with col2:
                        st.markdown("""The Budget of California VS 
                        the amount set aside for the Department of Water Resources.
                        Hovering over the bars reveals tooltips with additional information.""")
                        
                        title = alt.TitleParams('Budget of California Vs % used by DWR', anchor = 'middle')
                        bar_chart = alt.Chart(budget1994,title=title).mark_bar().encode(
                            x="years:O",
                            y=alt.Y("state_budget",title ='Budget of California'),
                            color =alt.Color('state_budget', scale=alt.Scale(scheme='yellowgreenblue',zero=False),legend=None),
                            tooltip=[alt.Tooltip('DWR', title="DWR Budget "),
                                    alt.Tooltip("% of budget to DWR", title= '% of budget to DWR')])
                        layer = alt.Chart(budget1994).mark_bar().encode(
                            x="years:O",
                            y="entire_budget:Q",
                            tooltip=[alt.Tooltip('state_budget', title="State budget ")]
                            )
                        st.altair_chart(bar_chart+ layer, use_container_width=True)
                        st.markdown("""The rankings of the populations
                        of each county as bars and the rankings 
                        of the numbers of stations per county as circles.
                        Note, for population, higher ranking means higher population.
                        And if station count is missing. It was not in the data itself.""")
                        title = alt.TitleParams('County population means VS station counts', anchor = 'middle')
                        not_bar = alt.Chart(poola,title=title).mark_bar().encode(
                            y =alt.Y('County', sort = None),
                            x=alt.X("Population_rank",title ='Population rank of county'),
                            color =alt.Color('Population_rank', scale=alt.Scale(scheme='blueorange',zero=False),legend=None),
                            tooltip=[alt.Tooltip('County', title="Name of County: "),
                                    alt.Tooltip('Population', title=" mean population "),
                                    alt.Tooltip('Population_rank')])
                        layers = alt.Chart(poola).mark_circle().encode(
                            y =alt.Y('County', sort = None),
                            x="Station rank:Q",
                            tooltip=[alt.Tooltip('Station count', title="Station count "),
                                    alt.Tooltip("Station rank", title= 'Station rank')])
                        st.altair_chart(not_bar+layers,use_container_width=True)
    if years == "2004-2013":
            with col1:
        
                st.markdown("""A color map, of the counts of testing stations for the DWR 
                        in California counties. 
                        The tooltips can be hidden by 
                        hovering over the layers icon in the upper right hand of the map.
                        As the counts increase the color deepens, if no stations are counted,
                        the color of the county will display as gray.
                        """)
                st_data = st_folium(m10)
                st.dataframe(data=pl,height=300)                                                                                                                                                       
                with col3:
                    st.markdown("""A dataframe of California's budget data, 
                        containing the total state budget (in dollars),
                        how much was alloted to the DWR, 
                        and what % that ended up being. """)
                    st.dataframe(budget2004percent,height=280)
                    st.markdown("""A dataframe of California's population data. The mean population was calculated.
                        Each population was ranked, 
                        and the number of testing stations was also ranked.""")
                    st.dataframe(poolb,height=280)
                    with col2:
                        st.markdown("""The Budget of California VS 
                        the amount set aside for the Department of Water Resources.
                        Hovering over the bars reveals tooltips with additional information.""")
                        title = alt.TitleParams('Budget of California Vs % used by DWR', anchor = 'middle')
                        bar_chart = alt.Chart(budget2004,title=title).mark_bar().encode(
                            x="years:O",
                            y=alt.Y("state_budget",title ='Budget of California'),
                            color =alt.Color('state_budget', scale=alt.Scale(scheme='yellowgreenblue',zero=False),legend=None),
                            tooltip=[alt.Tooltip('DWR', title="DWR Budget "),
                                    alt.Tooltip("% of budget to DWR", title= '% of budget to DWR')])
                        layer = alt.Chart(budget2004).mark_bar().encode(
                            x="years:O",
                            y="entire_budget:Q",
                            tooltip=[alt.Tooltip('state_budget', title="State budget ")]
                            )
                        st.altair_chart(bar_chart+ layer, use_container_width=True)
                        st.markdown("""The rankings of the populations
                        of each county as bars and the rankings 
                        of the numbers of stations per county as circles.""")
                        title = alt.TitleParams('County population means VS station counts', anchor = 'middle')
                        not_bar = alt.Chart(poolb,title=title).mark_bar().encode(
                            y =alt.Y('County', sort = None),
                            x=alt.X("Population_rank",title ='Population rank of county'),
                            color =alt.Color('Population_rank', scale=alt.Scale(scheme='blueorange',zero=False),legend=None),
                            tooltip=[alt.Tooltip('County', title="Name of County: "),
                                    alt.Tooltip('Population', title=" mean population "),
                                    alt.Tooltip('Population_rank')])
                        layers = alt.Chart(poolb).mark_circle().encode(
                            y =alt.Y('County', sort = None),
                            x="Station rank:Q",
                            tooltip=[alt.Tooltip('Station count', title="Station count "),
                                    alt.Tooltip("Station rank", title= 'Station rank')])
                        st.altair_chart(not_bar+layers,use_container_width=True)
    if years == "2014-2023":
        with col1:
        
                st.markdown("""A color map, of the counts of testing stations for the DWR 
                        in California counties. 
                        The tooltips can be hidden by 
                        hovering over the layers icon in the upper right hand of the map.
                        As the counts increase the color deepens, if no stations are counted,
                        the color of the county will display as gray.
                        """)
                st_data = st_folium(m11)
                st.dataframe(data=pm,height=300)                                                                                                                                                       
                with col3:
                    st.markdown("""A dataframe of California's budget data, 
                        containing the total state budget (in dollars),
                        how much was alloted to the DWR, 
                        and what % that ended up being. """)
                    st.dataframe(budget2023percent,height=280)
                    st.markdown("""A dataframe of California's population data. The mean population was calculated.
                        Each population was ranked, 
                        and the number of testing stations was also ranked.""")
                    st.dataframe(poolc,height=280)
                    with col2:
                        st.markdown("""The Budget of California VS 
                        the amount set aside for the Department of Water Resources.
                        Most of this decade, the budget for DWR was so insignificant
                        that it won't even appear as a data point.
                        Hovering over the bars reveals tooltips with additional information.""")
                        title = alt.TitleParams('Budget of California Vs % used by DWR', anchor = 'middle')
                        bar_chart = alt.Chart(budget2023,title=title).mark_bar().encode(
                            x="years:O",
                            y=alt.Y("state_budget",title ='Budget of California'),
                            color =alt.Color('state_budget', scale=alt.Scale(scheme='yellowgreenblue',zero=False),legend=None),
                            tooltip=[alt.Tooltip('DWR', title="DWR Budget "),
                                    alt.Tooltip("% of budget to DWR", title= '% of budget to DWR')])
                        layer = alt.Chart(budget2023).mark_bar().encode(
                            x="years:O",
                            y="entire_budget:Q",
                            tooltip=[alt.Tooltip('state_budget', title="State budget ")]
                            )
                        st.altair_chart(bar_chart+ layer, use_container_width=True)
                        st.markdown("""The rankings of the populations
                        of each county as bars and the rankings 
                        of the numbers of stations per county as circles.
                        And if station count is missing. It was not in the data itself.""")
                        title = alt.TitleParams('County population means VS station counts', anchor = 'middle')
                        not_bar = alt.Chart(poolc,title=title).mark_bar().encode(
                            y =alt.Y('County', sort = None),
                            x=alt.X("Population_rank",title ='Population rank of county'),
                            color =alt.Color('Population_rank', scale=alt.Scale(scheme='blueorange',zero=False),legend=None),
                            tooltip=[alt.Tooltip('County', title="Name of County: "),
                                    alt.Tooltip('Population', title=" mean population "),
                                    alt.Tooltip('Population_rank')])
                        layers = alt.Chart(poolc).mark_circle().encode(
                            y =alt.Y('County', sort = None),
                            x="Station rank:Q",
                            tooltip=[alt.Tooltip('Station count', title="Station count "),
                                    alt.Tooltip("Station rank", title= 'Station rank')])
                        st.altair_chart(not_bar+layers,use_container_width=True)
        

page_names_to_funcs = {
    "Introduction": main_page,
    "Final Project": page2,
    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()