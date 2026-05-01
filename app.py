import streamlit as st
import pandas as pd
import joblib

model = joblib.load('water_potability_model (2).pkl')
scaler = joblib.load('scaler.pkl')
st.title(" Water Potability Prediction")
st.write("Enter the water characteristics below to check if it's safe to drink or not")

ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
solids = st.number_input("Solids", min_value=0.0, value=20000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=15.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=60.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

if st.button("Predict Potability"):
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, 
                                conductivity, organic_carbon, trihalomethanes, turbidity]], 
                              columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                                       'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
    
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)

    st.markdown("---")
    if prediction[0] == 1:
        st.success(" The water is Potable (Safe to drink)")
    else:
        st.error(" The water is not Potable (Unsafe to drink)")
