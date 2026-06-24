# app.py
import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Prediksi Harga Laptop", page_icon="💻")
st.title("💻 Laptop Price Predictor")

# Load model
@st.cache_resource
def load_model():
    with open('Laptop_price_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# Input form
with st.form("laptop_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        brand = st.selectbox("Brand", ["Asus", "Lenovo", "HP", "Dell", "Apple", "Acer"])
        processor = st.selectbox("Processor", ["Intel i3", "Intel i5", "Intel i7", "Intel i9", 
                                                "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1", "Apple M2"])
        ram = st.slider("RAM (GB)", 4, 64, 16, step=4)
        storage = st.slider("Storage (GB)", 128, 2048, 512, step=128)
    
    with col2:
        gpu = st.selectbox("GPU", ["Integrated", "NVIDIA RTX 3050", "NVIDIA RTX 3060",
                                    "NVIDIA RTX 4060", "NVIDIA RTX 4070"])
        screen = st.slider("Screen Size (inch)", 13.3, 17.3, 15.6, step=0.3)
        os = st.selectbox("OS", ["Windows 11", "macOS", "Linux", "No OS"])
        weight = st.slider("Weight (kg)", 1.0, 4.0, 1.8, step=0.1)
    
    submitted = st.form_submit_button("Prediksi Harga 🔮")

if submitted:
    input_df = pd.DataFrame([{
        'Brand': brand, 'Processor': processor, 'RAM_GB': ram,
        'Storage_GB': storage, 'GPU': gpu, 'Screen_Size_inch': screen,
        'OS': os, 'Weight_kg': weight
    }])
    
    price = model.predict(input_df)[0]
    st.success(f"💰 Prediksi Harga: **Rp {price:,.0f}**")
