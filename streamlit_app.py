import pandas as pd
import streamlit as st
import plotly.express as px

original_DF = pd.read_csv('Consult_Summary_Report_-_CP.csv')
original_DF['timeBetweenAcceptandCompletion'] = original_DF['updatedTime'].sub(original_DF['createdTime'])
original_DF.head(n=10)
st.title("Carolina Pines Patient Report Data: Interactive")
st.dataframe(original_DF, use_container_width=True)
columns = st.multiselect("Select columns to display", options=original_DF.columns, default=list(original_DF.columns))
filtered_df = original_DF[columns]


numeric_columns = original_DF.select_dtypes(include='number').columns
categorical_columns = original_DF.select_dtypes(include='object').columns
num_column = st.selectbox('Select a column to display on the histogram', numeric_columns)
cat_column = st.selectbox('Select a column to display on the bar chart', categorical_columns)

if num_column:
    fig_1 = px.histogram(original_DF, x=num_column, title= f'Distribution of {num_column}')
    st.plotly_chart(fig_1, use_container_width=True, theme="streamlit")

if cat_column:
    fig_2 = st.bar(original_DF[cat_column], y=cat_column, title=f'Frequency of {cat_column}')
    st.bar_chart(fig_2, use_container_width=True)
