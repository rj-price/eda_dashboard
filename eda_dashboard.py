import pandas as pd
import seaborn as sns
import streamlit as st

# Set page config
st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊"
)

# Title and description
st.title("📊 EDA Dashboard")
st.markdown("Interactive dashboard for exploratory data analysis and visualisation.")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("./assemblies.csv", index_col=0)

data = load_data()
headers = list(data)

# Custom CSS to improve appearance
st.markdown("""
    <style>
    .stButton>button {
        width: 80%;
        margin: 0 10%; 
    }
    </style>
""", unsafe_allow_html=True)

# Create three columns for the buttons
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    show_data = st.button("Show Data")
with col2:
    show_summary = st.button("Show Summary")
with col3:
    show_missing = st.button("Show Missing Values")

# Display data based on button clicks
if show_data:
    st.dataframe(data, use_container_width=True)
if show_summary:
    st.dataframe(data.describe(), use_container_width=True)
if show_missing:
    missing_df = pd.DataFrame({
        'Missing Values': data.isna().sum(),
        'Percentage': (data.isna().sum() / len(data) * 100).round(2)
    })
    st.dataframe(missing_df, use_container_width=True)

### NOTE ###
# If wanting to include additional data on barchart or scatterplot
# Need conditionals, or buttons (ie. for barplot, button 1 ar, button for 2 bars, button for 3)

st.markdown("<br>", unsafe_allow_html=True)

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs(["Correlation Analysis", "Distribution Analysis", "Bar Charts", "Scatter Plots"])

####### Correlation #######
with tab1:
    st.write("## Correlation Matrix and Heatmap")
    if st.button("Show Correlation"):
        st.dataframe(data.corr(), use_container_width=True)
        corr_plot = sns.heatmap(data.corr(), annot=True)
        st.pyplot(corr_plot.get_figure())

####### Histogram #######
with tab2:
    st.write("## Histogram")
    hist_column = st.selectbox("Choose which data to plot as histogram:", headers)
    if st.button("Plot Histogram"):
        hist_plot = sns.histplot(data=data, x=hist_column)
        st.pyplot(hist_plot.get_figure())

####### Barchart #######
with tab3:
    st.write("## Barchart")
    bar_column = st.selectbox("Choose which data to plot as barchart:", headers)
    if st.button("Plot Barchart"):
        st.bar_chart(data[bar_column])
    
####### Scatterplot #######
with tab4:
    st.write("## Scatterplot")
    scatter_x = st.selectbox("Choose which data to plot on X axis:", headers)
    scatter_y = st.selectbox("Choose which data to plot on Y axis:", headers)
    if st.button("Plot Scatterplot"):
        st.scatter_chart(data=data, x=scatter_x, y=scatter_y)
    

# Add footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Built by Jordan Price (2025). Powered by Streamlit</p>", unsafe_allow_html=True)
