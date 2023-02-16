import streamlit as st
import pandas as pd
import pickle


xgb_model = pickle.load(open("xgb_model.sav", "rb"))

st.title("used car price prediction")

brand = st.selectbox(
	"Brand",
	("Audi","BMW","Bently","Chevrolet","Datsun","Fiat","Force","Ford","Honda","Hyundai","Isuzu","Jeep","Kia","Land","Lexus","MG","Mahindra","Maruthi","Maserati","merceses-Benz","Mini","Mitsubishi","Nissan","Porsche","Premier","Renault","skoda","Tata","Toyata","Volkswagen")
)
kms_driven = st.number_input("KMS driven")