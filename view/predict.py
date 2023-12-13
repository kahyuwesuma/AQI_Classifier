import streamlit as st
import json

st.set_page_config(
    page_title="AQI Classifier",
    page_icon="📈",
)

def load_json(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        st.error(f"Error loading JSON file: {e}")
        return None

aqi_data = load_json('data/cluster.json')

def input_with_category(column1, column2, label, category_label, category_data):
    value = column1.number_input(label)
    
    # Otomatis dapatkan kategori berdasarkan nilai yang dimasukkan
    default_category = get_category_from_value(value, category_data)
    category = column2.number_input(category_label, min_value=0, max_value=len(category_data)-1, value=default_category)
    
    return value, category

def get_category_from_value(value, category_data):
    for category_info in category_data:
        if category_info["range"][0] <= value <= category_info["range"][1]:
            return category_info["category"]
    return None

def inputs(model, aqi_data):
    country = st.text_input("Input Your Country")
    city = st.text_input("Input Your City")

    col1, col2 = st.columns([2, 1])

    aqi_value, aqi_category = input_with_category(col1, col2, "AQI Value", "AQI Category", aqi_data["categories"]["AQI_Value"])
    co_aqi_value, co_aqi_category = input_with_category(col1, col2, "CO AQI Value", "CO AQI Category", aqi_data["categories"]["CO_AQI_Value"])
    ozone_aqi_value, ozone_aqi_category = input_with_category(col1, col2, "Ozone AQI Value", "Ozone AQI Category", aqi_data["categories"]["Ozone_AQI_Value"])
    no2_aqi_value, no2_aqi_category = input_with_category(col1, col2, "NO2 AQI Value", "NO2 AQI Category", aqi_data["categories"]["NO2_AQI_Value"])
    pm25_aqi_value, pm25_aqi_category = input_with_category(col1, col2, "PM2.5 AQI Value", "PM2.5 AQI Category", aqi_data["categories"]["PM2.5_AQI_Value"])

    if st.button("Predict"):
        if all([aqi_value, aqi_category, co_aqi_value, co_aqi_category,
                ozone_aqi_value, no2_aqi_value, no2_aqi_category, pm25_aqi_value, pm25_aqi_category]):
            # Predict Inputs
            input_data = [[aqi_value, aqi_category, co_aqi_value, co_aqi_category,
                        ozone_aqi_value, ozone_aqi_category, no2_aqi_value, no2_aqi_category,
                        pm25_aqi_value, pm25_aqi_category]]

            prediction = model.predict(input_data)

            # Showing Results
            st.success(f"Negara {country}, Kota {city}, Termasuk ke dalam Cluster: {prediction[0]}")
            prediction_message = (
                'Your Area is Healthy' if prediction[0] == 0
                else 'Your Area is Unhealthy' if prediction[0] == 1
                else 'Your Area is Moderate' if prediction[0] == 2
                else 'Unknown Prediction'
            )

            icon = (
                '🥰' if prediction[0] == 0
                else '😔' if prediction[0] == 1
                else '😊' if prediction[0] == 2
                else '❓'
            )

            st.toast(prediction_message, icon=icon)
        else:
            # Tampilkan peringatan jika ada input yang belum terisi
            st.warning("Please fill in all the required inputs.")
