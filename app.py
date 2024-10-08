import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(
  page_title="AR/VR powered Immersive Study Space",
  page_icon="📚",
  layout="wide",
  initial_sidebar_state="expanded")

alt.themes.enable("dark")

df=pd.read_csv('AR VR Spaces Responses.csv')

st.title('AR/VR powered Immersive Study Space 📚')
