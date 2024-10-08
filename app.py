import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from annotated_text import annotated_text


st.set_page_config(
  page_title="AR/VR powered Immersive Study Space",
  page_icon="📚",
  layout="wide",
  initial_sidebar_state="expanded")

alt.themes.enable("dark")

df=pd.read_csv('responses.csv')

st.title('AR/VR powered Immersive Study Space 📚')
#st.image('books.png',use_column_width=True)

st.subheader('1. Meet or stakeholders.')
