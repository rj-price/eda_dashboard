import streamlit as st
import pandas as pd

file_path = "./assemblies.csv"

st.title("EDA Dashboard")
data = pd.read_csv(file_path, index_col=0)
headers = list(data)

if st.button("Show Data"):
    st.write(data)
    
if st.button("Show Summary"):
    st.write(data.describe())

# Barchart
st.write("## Barchart")
selected_column = st.selectbox("Choose which data to plot:", headers)

if st.button("Plot Barchart"):
    st.bar_chart(data[selected_column])
    
# Scatterplot
st.write("## Scatterplot")
scatter_x = st.selectbox("Choose which data to plot on X axis:", headers)
scatter_y = st.selectbox("Choose which data to plot on Y axis:", headers)

if st.button("Plot Scatterplot"):
    st.scatter_chart(data=data, x=scatter_x, y=scatter_y)