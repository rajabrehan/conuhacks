import streamlit as st
import pandas as pd
import requests
from config import GOOGLE_MAPS_API_KEY

st.set_page_config(layout="wide")

col1, col2 = st.columns([2, 5])

with col1:

    st.header("Select Your Dietary Preferences")
    
    halal = st.checkbox("Halal")
    vegan = st.checkbox("Vegan")

    selected_restrictions = []
    if vegan:
        selected_restrictions.append("Vegan")
    if halal:
        selected_restrictions.append("Halal")

with col2:
    # Data frame with location of Quebec City
    data = pd.DataFrame({
        'lat': [45.5017],
        'lon': [-73.5673]
    })

    st.map(data)
