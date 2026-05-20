import streamlit as st
import pickle 


st.title ("House Price Prediction ML App")

area = pickle.load(open("area.pkl","rb"))  #run binary

area_sq = st.number_input("Enter an area in SQ-FT",min_value=500)


if st.button("Predict Price"):
    input_data = [[area_sq]]
    predicted_price = area.predict(input_data)
    st.success(f"Your Predicted Price For {area_sq} is : {predicted_price[0]}")