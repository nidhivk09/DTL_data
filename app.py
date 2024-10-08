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
#st.image('books.png',use_column_width=True)

st.write(" Over the past 2 weeks we conducted a survey whoch garnered more than 150 responses and recorded 40+ interviews. Following dashboard shows the data visualisation of the dta that was collected. This data will aid us to develop and product and incorporate most of the user requested features to make it an inclusive product that creates a differnec in evry user's life.")

st.subheader('1. Meet our stakeholders.')

st.image('role.png')

st.subheader('2. How do they study/ work')

st.image('howstudy.png')
