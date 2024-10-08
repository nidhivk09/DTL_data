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

df=pd.read_csv('responses.csv')

st.title('AR/VR powered Immersive Study Space 📚')
st.image('lofigirl.png',use_column_width=True)

st.subheader('1. Meet or stakeholders.')
