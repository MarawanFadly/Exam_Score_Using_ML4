import os
import numpy as np
import pandas as pd
import streamlit as st      # streamlit run app/app.py
import joblib 
import pickle


#model= joblib.load("../app/artifacts/svm_pipeline.pkl")

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

df=pd.read_csv('./data/feature eng data/feature_eng_data.csv')

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

box_31, box_32, box_33 =   st.columns( 3 )

facility_rating = box_31.selectbox( 'facility_rating',
          options = df['facility_rating'].unique())

exam_difficulty = box_32.selectbox( 'exam_difficulty',
          options = df['exam_difficulty'].unique())

exam_score=box_33.slider( 'exam_score',
              min_value= df['exam_score'].min(),
              max_value= df['exam_score'].max())


# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        'gender', 'course', 'study_hours', 'class_attendance',
        'internet_access', 'sleep_hours', 'sleep_quality',
        'study_method', 'facility_rating', 'exam_difficulty', 'exam_score'
    ])

# Create row
input_data = pd.DataFrame([{
    'gender': gender,
    'course': course,
    'study_hours': study_hours,
    'class_attendance': class_attendance,
    'internet_access': internet_access,
    'sleep_hours': sleep_hours,
    'sleep_quality': sleep_quality,
    'study_method': study_method,
    'facility_rating': facility_rating,
    'exam_difficulty': exam_difficulty,
    'exam_score': exam_score
}])


st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;  /* Green background */
        color: white;               /* White text */
        height: 3em;
        width: 100%;
        border-radius: 10px;
        margin-left:100%;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Data", key="add_data_button"):
        st.session_state.data.loc[len(st.session_state.data)] = input_data.iloc[0]

with col2:
    if st.button("Clear Table", key="clear_data_button"):
        st.session_state.data = st.session_state.data.iloc[0:0]

# Display table
st.dataframe(st.session_state.data)