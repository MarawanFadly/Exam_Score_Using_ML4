import os
import numpy as np
import pandas as pd
import streamlit as st      # streamlit run app/app.py
import joblib
import pickle

model= joblib.load("../artifacts/svm_pipeline.pkl")

st.set_page_config( 'Exam Score Prediction', ':book:', 'wide' )

#### Setting a background color to a streamlit page

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #9ddf93; 
}
</style>
""", unsafe_allow_html=True)

st.markdown( '<h1 style ="font-size:50px;color:white;background-color:brown;text-align:center;font-family:times new roman;" >Exam Score Prediction using ML</h1>', unsafe_allow_html=True )

df=pd.read_csv('../data/feature eng data/feature_eng_data.csv')

box_11, box_12, box_13, box_14 =   st.columns( 4 )

# Row 1

gender = box_11.selectbox( 'gender',
             options = df['gender'].unique())

course = box_12.selectbox( 'Course',
             options = df['course'].unique())

study_hours = box_13.slider( 'Study Hours',
          min_value= df['study_hours'].min(),
          max_value= df['study_hours'].max())

class_attendance = box_14.slider( 'class_attendance',
          min_value= df['class_attendance'].min(),
          max_value= df['class_attendance'].max())

# Row 2

box_21, box_22, box_23, box_24 =   st.columns( 4 )

internet_access = box_21.selectbox( 'internet_access',
             options = df['internet_access'].unique())

sleep_hours = box_22.slider( 'sleep_hours',
              min_value= df['sleep_hours'].min(),
              max_value= df['sleep_hours'].max())

sleep_quality = box_23.selectbox( 'sleep_quality',
          options = df['sleep_quality'].unique())

study_method = box_24.selectbox( 'study_method',
          options = df['study_method'].unique())

# Row 3

box_31, box_32 =   st.columns( 2 )

facility_rating = box_31.selectbox( 'facility_rating',
          options = df['facility_rating'].unique())

exam_difficulty = box_32.selectbox( 'exam_difficulty',
          options = df['exam_difficulty'].unique())

# st.write( gender, course, study_hours, class_attendance )         # Just for test !

columns = [
    'index',
    'study_hours',
    'class_attendance',
    'sleep_hours',
    'sleep_quality',
    'facility_rating',
    'exam_difficulty',
    'exam_score',
    'course_diff'
]
data=pd.DataFrame(columns=columns)
st.dataframe(data)