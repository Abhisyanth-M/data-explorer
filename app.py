import streamlit as st
import pandas as pd

st.title("Smart Data Explorer Dashboard")
st.write("DATA EXPLORER DASHBOARD")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write(f"Total number of rows: {len(df)}")

    selected_column = st.selectbox("Select a column:", df.columns)
    st.write(f"Data type of {selected_column} is {df[selected_column].dtype}")

    selected_value = st.selectbox(
        "Select a value",
        df[selected_column].unique()
    )

    filtered_df = df[df[selected_column] == selected_value]

    st.write(f"Number of null values in {selected_column} is {df[selected_column].isnull().sum()}")

    st.write(f"Showing data where {selected_column} = {selected_value}")
    st.dataframe(filtered_df)

    st.write("### Data Preview")
    st.dataframe(df)

    st.write("### Basic Info")
    st.write(df.describe())