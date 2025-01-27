import pandas as pd
import seaborn as sns
import streamlit as st

file_path = "./assemblies.csv"

# Set page title and icon
st.set_page_config(page_title="EDA Dashboard", page_icon="💾")

# Title, import data and extract header names
st.title("EDA Dashboard")
data = pd.read_csv(file_path, index_col=0)
headers = list(data)

# Show all data on button
if st.button("Show Data"):
    st.write(data)

# Show data summary on button
if st.button("Show Summary"):
    st.write(data.describe())
    
# Show missing data on button
if st.button("Show Missing"):
    st.write(data.isna().sum())

### NOTE ###
# If wanting to include additional data on barchart or scatterplot
# Need conditionals, or buttons (ie. for barplot, button 1 ar, button for 2 bars, button for 3)

####### Correlation #######
st.write("## Correlation Matrix and Heatmap")
if st.button("Show Correlation"):
    st.write(data.corr())
    corr_plot = sns.heatmap(data.corr(), annot=True)
    st.pyplot(corr_plot.get_figure())

####### Histogram #######
st.write("## Histogram")
hist_column = st.selectbox("Choose which data to plot as histogram:", headers)
if st.button("Plot Histogram"):
    hist_plot = sns.histplot(data=data, x=hist_column)
    st.pyplot(hist_plot.get_figure())

####### Barchart #######
st.write("## Barchart")
bar_column = st.selectbox("Choose which data to plot as barchart:", headers)

if st.button("Plot Barchart"):
    st.bar_chart(data[bar_column])
    
####### Scatterplot #######
st.write("## Scatterplot")
scatter_x = st.selectbox("Choose which data to plot on X axis:", headers)
scatter_y = st.selectbox("Choose which data to plot on Y axis:", headers)

if st.button("Plot Scatterplot"):
    st.scatter_chart(data=data, x=scatter_x, y=scatter_y)
    

# Add footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Built by Jordan Price (2025). Powered by Streamlit</p>", unsafe_allow_html=True)
