import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

# Load the filtered data
df = pd.read_excel('/mnt/data/AR VR Study Spaces Responses.xlsx', sheet_name='Form Responses 1')
filtered_df = df[[
    "What describes you the best ?",
    "How would you describe your study habits?",
    "How many hours a day do you spend on self study/up-skilling?",
    "Do you have a dedicated study space?",
    "What does your current study or work environment look like?",
    "What features would you want to have in your ideal immersive study environment?"
]]

st.title("AR/VR Immersive Study Space Survey Analysis")

# Section 1: Participant Role Distribution
st.subheader("Participant Role Distribution")
role_counts = filtered_df['What describes you the best ?'].value_counts()
fig, ax = plt.subplots()
ax.pie(role_counts, labels=role_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Section 2: Study Habits Distribution
st.subheader("Study Habits Distribution")
study_habits_counts = filtered_df['How would you describe your study habits?'].value_counts()
fig, ax = plt.subplots()
ax.barh(study_habits_counts.index, study_habits_counts.values, color='skyblue')
ax.set_xlabel("Number of Participants")
st.pyplot(fig)

# Section 3: Self-Study/Up-Skilling Hours
st.subheader("Self-Study/Up-Skilling Hours")
study_hours_counts = filtered_df['How many hours a day do you spend on self study/up-skilling?'].value_counts()
fig, ax = plt.subplots()
ax.bar(study_hours_counts.index, study_hours_counts.values, color='lightgreen')
ax.set_ylabel("Number of Participants")
ax.set_xlabel("Hours Spent on Self-Study")
st.pyplot(fig)

# Section 4: Dedicated Study Space
st.subheader("Dedicated Study Space")
space_counts = filtered_df['Do you have a dedicated study space?'].value_counts()
fig, ax = plt.subplots()
ax.pie(space_counts, labels=space_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Section 5: Study/Work Environment
st.subheader("Current Study/Work Environment")
environments = filtered_df['What does your current study or work environment look like?'].dropna()
env_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(environments))
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(env_wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Section 6: Features of Ideal Immersive Study Environment
st.subheader("Features in Ideal Immersive Study Environment")
features = filtered_df['What features would you want to have in your ideal immersive study environment?'].dropna()
features_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(features))
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(features_wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

