import streamlit as st
import pandas as pd
import joblib

model = joblib.load('water_potability_model (2).pkl')

st.title(" Water Potability Prediction")
st.write("Enter the water characteristics below to check if it's safe to drink or not")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
    hardness = st.number_input("Hardness (mg/L)", min_value=0.0, value=150.0)
    solids = st.number_input("Solids (ppm)", min_value=0.0, value=20000.0)

with col2:
    chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, value=7.0)
    sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=300.0)
    conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, value=400.0)

with col3:
    organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, value=15.0)
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, value=60.0)
    turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=4.0)

if st.button("Predict Potability"):
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, 
                                conductivity, organic_carbon, trihalomethanes, turbidity]], 
                              columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                                       'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
    
    prediction = model.predict(input_data)
    

    st.markdown("---")
    if prediction[0] == 1:
        st.success(" The water is Potable (Safe to drink)")
    else:
        st.error(" The water is not Potable (Unsafe to drink)")
