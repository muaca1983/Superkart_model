import streamlit as st
import requests
import json
import pandas as pd

st.set_page_config(page_title="SuperKart Sales Prediction", layout="wide")

st.title("SuperKart Sales Prediction App")
st.markdown("Predict total product sales using trained machine learning models.")

# Backend API endpoint URL
BACKEND_URL = "http://backend:7860/v1/predict"

st.sidebar.header("Product & Store Details")

# Form input fields
product_weight = st.sidebar.number_input("Product Weight", min_value=0.0, value=12.5, step=0.1)
product_sugar = st.sidebar.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
product_allocated_area = st.sidebar.number_input("Product Allocated Area Ratio", min_value=0.0, max_value=1.0, value=0.05, step=0.001)
product_type = st.sidebar.selectbox("Product Type", [
    "Frozen Foods", "Dairy", "Canned", "Baking Goods", "Health and Hygiene", 
    "Snack Foods", "Meat", "Soft Drinks", "Household", "Others"
])
product_mrp = st.sidebar.number_input("Product MRP ($)", min_value=0.0, value=150.0, step=1.0)
store_size = st.sidebar.selectbox("Store Size", ["Small", "Medium", "High"])
store_city_type = st.sidebar.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
store_type = st.sidebar.selectbox("Store Type", ["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"])
product_id_char = st.sidebar.selectbox("Product ID Prefix", ["FD", "DR", "NC"])
store_age_years = st.sidebar.number_input("Store Age (Years)", min_value=0, max_value=100, value=15, step=1)
if st.button("Predict Sales"):
    payload = {
        "Product_Id": f"{product_id_char}15",  # <-- Added missing column
        "Store_Id": "OUT049",                 # <-- Added missing column
        "Product_Weight": float(product_weight),
        "Product_Sugar_Content": str(product_sugar),
        "Product_Allocated_Area": float(product_allocated_area),
        "Product_Type": str(product_type),
        "Product_MRP": float(product_mrp),
        "Store_Size": str(store_size),
        "Store_Location_City_Type": str(store_city_type),
        "Store_Type": str(store_type),
        "Product_Id_char": str(product_id_char),
        "Store_Age_Years": float(store_age_years)
    }

    try:
        response = requests.post(BACKEND_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"### Predicted Total Sales: ${result['prediction']:.2f}")
        else:
            st.error(f"Error from API: {response.text}")
    except Exception as e:
        st.error(f"Could not connect to backend server: {e}")
