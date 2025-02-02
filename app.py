import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Sidebar for dietary restrictions
st.sidebar.header("Select Your Dietary Preferences")
with st.sidebar.expander("Dietary Preferences", expanded=True):
    dietary_preferences = {
        "Vegan": st.sidebar.checkbox("Vegan"),
        "Lactose-Free": st.sidebar.checkbox("Lactose-Free"),
        "Gluten-Free": st.sidebar.checkbox("Gluten-Free"),
        "Halal": st.sidebar.checkbox("Halal")
    }

selected_preferences = [key for key, value in dietary_preferences.items() if value]

def display_map():
    # Data frame with location of Quebec City
    data = pd.DataFrame({
        'lat': [45.5017],
        'lon': [-73.5673]
    })

    st.map(data)



display_map()