from model.aqi_model import load_aqi_model
from view.cluster_info_view import display_cluster_info
from view.predict import inputs, load_json
import streamlit as st
import json

def main():   
    try:
        model = load_aqi_model('model/aqi_predictor_model.sav')
        aqi_data = load_json('data/category.json')
        page = st.sidebar.selectbox("Menu", ["Prediction" ,"Cluster Information"])      
        if page == "Prediction":
            inputs(model, aqi_data)
        elif page == "Cluster Information":
            display_cluster_page()
    except Exception as e:
        st.error(f"Error loading the model: {e}")

def display_cluster_page():
    try:
        with open('data/cluster.json', "r") as cluster_file:
            cluster_info_data = json.load(cluster_file)
        display_cluster_info(cluster_info_data)
    except Exception as e:
        st.error(f"Error loading the JSON: {e}")