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

st.header('Visualization of California water testing Data over the last 100 years')

st.image('number_of_testing_stations_over_100_years.png')

st.header('Visualization of California water testing Data over the last 100 years')

st.image('Number of types of tests over the last 100 years.png')



f = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\lab_results_a.csv")
b = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\stations_a.csv")
c = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\field_results_a.csv")
d = pd.read_csv(r"C:\Users\amcfa\gitfiles\Projects\MastersWork\FundamentalssofDataVisualizzations\period_of_record_a.csv")


