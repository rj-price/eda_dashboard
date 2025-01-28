import pandas as pd
import plotly.express as px
import streamlit as st

# Set page config
st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊"
)

# Title and description
st.title("📊 EDA Dashboard")
st.markdown("""
            <p style="font-size:1.3rem">
            Interactive dashboard for rapid exploratory data analysis (EDA) and 
            visualisation of tabular numerical data.</p>
            """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Load data
st.write("## Upload Data")
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file, index_col=0)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file, index_col=0)
        st.success('File successfully uploaded!')
    except Exception as e:
        st.error(f'Error: {e}')
        st.stop()
else:
    try:
        data = load_data("./assemblies.csv")
        st.info('Using default dataset. Upload your own CSV file above to analyse different data.')
    except Exception as e:
        st.error(f'Error: Could not load default file. Please upload a CSV file.')
        st.stop()
        
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

show_data = col1.button("Show Data")
show_summary = col2.button("Show Summary")
show_missing = col3.button("Show Missing Values")

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
    st.write("## Correlation Analysis")
    if st.button("Generate Correlation Matrix"):
        corr_matrix = data.corr()
        fig = px.imshow(
            corr_matrix,
            color_continuous_scale='RdBu',
            aspect='auto',
            title='Correlation Matrix'
        )
        st.plotly_chart(fig, use_container_width=True)

####### Histogram #######
with tab2:
    st.write("## Distribution Analysis")
    hist_column = st.selectbox("Select variable for histogram:", headers)
    fig = px.histogram(
        data,
        x=hist_column,
        title=f'Distribution of {hist_column}',
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)

####### Barchart #######
with tab3:
    st.write("## Bar Charts")
    bar_column = st.selectbox("Select variable for bar chart:", headers)
    fig = px.bar(
        data,
        y=bar_column,
        title=f'Bar Chart of {bar_column}',
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
####### Scatterplot #######
with tab4:
    st.write("## Scatter Plots")
    col1, col2 = st.columns(2)
    scatter_x = col1.selectbox("Select X-axis variable:", headers)
    scatter_y = col2.selectbox("Select Y-axis variable:", headers)
    fig = px.scatter(
        data,
        x=scatter_x,
        y=scatter_y,
        title=f'{scatter_y} vs {scatter_x}',
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)

# Add footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Built by Jordan Price (2025). Powered by Streamlit</p>", unsafe_allow_html=True)
