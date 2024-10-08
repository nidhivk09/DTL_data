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

st.write(" Over the past 2 weeks we conducted a survey whoch garnered more than 150 responses and recorded 40+ interviews. Following dashboard shows the data visualisation of the dta that was collected. This data will aid us to develop and product and incorporate most of the user requested features to make it an inclusive product that creates a difference in every user's life.")

st.subheader('**1. Meet our stakeholders.**')

st.image('role.png')
st.write("Analysis: almost 90 % of our users are students")



st.subheader('2. How do they study/ work?')

st.image('howstudy.png')



st.subheader('3. How much time do they spend on upskilling/ studying?')
st.image('studytime.png')




st.subheader('4. Do they have a dedicated study space?')

st.image('dedicatedstudyspace.png')




st.subheader('5. How is their current study space?')

st.image('currentstudy.png')




st.subheader('6. Does the current space motivate them to be productive?')

st.image('iscureentspacegood.png')



st.subheader('7.How familiar are our stakeholders about the AR/ VR technology?')
st.image('doyouknowarvr.png')



st.subheader('**8. Is it important to customize study space?**')

st.image('studyspacepersonal.png')




st.header('9. Are stakeholders open to integrate AR/VR to set up their study spaces?')

st.image('opentousearinstudt.png')




st.subheader('10. What are the main features to be included in the product?')

st.image('features.png')




st.subheader('11. Are the user willing to be a part in the testing pahse of the product development?')

st.image('betatester.png')



