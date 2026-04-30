import streamlit as st
import pandas as pd
import joblib

model = joblib.load('water_potability_model(2).pkl')

st.title(" Water Potability Prediction")
st.write("Enter the water characteristics below to check if it's safe to drink or not")

ph = st.number_input("pH Level")
hardness = st.number_input("Hardness")
solids = st.number_input("Solids")
chloramines = st.number_input("Chloramines")
sulfate = st.number_input("Sulfate")
conductivity = st.number_input("Conductivity")
organic_carbon = st.number_input("Organic Carbon")
trihalomethanes = st.number_input("Trihalomethanes")
turbidity = st.number_input("Turbidity")

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
