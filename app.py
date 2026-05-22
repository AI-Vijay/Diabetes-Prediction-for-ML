import streamlit as st
import pandas as pd
import numpy as np 
import joblib
import plotly.graph_objects as go 

 st.set_page_config(
    page_title="Diabetes Prediction",
    page_Icon="",
    layout="wide"
 )

 st.markdown(f"""
    <style>
    .main {padding: 0rem 1rem;}
    .stAlert {padding: 1rem; border-radius:0.5rem;}
    h1 {color=#1f77b4; padding-bottom: 1rem;}
    </style>
    """, unsafte_allow_html=True)
