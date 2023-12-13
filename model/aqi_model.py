def load_aqi_model(model_path):
    try:
        dtc = 'model/aqi_predictor_model.sav'
        with open(dtc, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
