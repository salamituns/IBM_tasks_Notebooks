import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
data_analysis = st.beta_container()

with header:
    st.title('Welcome to my awesome data science project')
    st.text('')
    st.text('In this project, we will look into the analysis of the US Economic data')


with dataset:
    st.header('Dashboard analysis of the US Economy')
    st.text('This dataset was retrieved from the IBM/Coursera data science course')

    eco_data = pd.read_csv('/Users/olatunde/Data_Science_AI_ML/Strive_School/Buildweek/clean_gdp.csv')
    st.write(eco_data.head())

    st.subheader('Rate of GDP chnage with time')
    change_current = pd.DataFrame(eco_data['change-current'].value_counts())
    st.bar_chart(change_current)



with features:
    st.header('The features we have created')


with data_analysis:
    st.header('Analysis of people, book and life')
    st.text('Here you get to choose different plots and see how people, books and life are inter-related with each other.')
