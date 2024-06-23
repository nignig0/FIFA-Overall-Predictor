import pickle as pkl
import pandas as pd
import streamlit as st

with open('model_pipeline.pkl', 'rb') as f:
    model = pkl.load(f)



st.set_page_config(page_title="FIFA Overall Predictor", layout="centered")

st.title("Enter the following information")

potential = st.number_input("Potential", min_value=0, max_value=100, value=50)
value_eur = st.number_input("Value in Euros", min_value=0.0, value=1000000.0)
wage_eur = st.number_input("Wage per week in euros", min_value=0.0, value=1000.0)
age = st.number_input("Age", min_value=0, value=20)
release_clause_eur = st.number_input("Release clause in EUR", min_value=0.0, value=10000000.0)
movement_reactions = st.number_input("Movement reactions attribute", min_value=0, max_value=100, value=50)

if st.button("Submit"):
    st.write("Potential:", potential)
    st.write("Value in Euros:", value_eur)
    st.write("Wage per week in Euros:", wage_eur)
    st.write("Age:", age)
    st.write("Release clause in EUR:", release_clause_eur)
    st.write("Movement reactions attribute:", movement_reactions)
    
    df = pd.DataFrame([{
        'potential': potential,
        'value_eur': value_eur,
        'wage_eur': wage_eur,
        'age':age,
        'release_clause_eur': release_clause_eur,
        'movement_reactions': movement_reactions
     }])
    prediction = model.predict(df)
    st.write("Predicted overall: ",  int(prediction[0]))

