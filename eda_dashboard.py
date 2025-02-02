import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    selected = option_menu(
            menu_title="EDA Dashboard",
            options=["About", "Features", "Usage"],
            icons=["info-circle", "list-ul", "question-circle"],
            menu_icon="clipboard-data",
            default_index=0,
        )

    if selected == "About":
        st.header("About")
        st.markdown(
            """
            EDA Dashboard is a Streamlit dashboard app for rapid exploratory data analysis (EDA) and visualisation of tabular data in `.csv` format.
            """
        )

    if selected == "Features":
        st.header("Features")
        st.markdown(
            """
            This app provides the following functionality:
            - Upload and analyse custom CSV files with automatic data type detection
            - View data, summary statistics and number of missing values per column
            - Generate a correlation matrix and heatmap
            - Visualise data distributions as histograms
            - Plot a selected column as a bar chart
            - Determine pairwise relationships between specified columns via scatterplots
            - Interactive plots with zoom, pan, and hover capabilities
            - Export visualisations as PNG files
            """
        )

    if selected == "Usage":
        st.header("Usage")
        st.markdown(
            """
            ### Data Upload
            The dashboard initially loads with example data (`assemblies.csv`) containing genome assembly metrics.

            To analyse your own data, click the "Upload your CSV file" button and select any CSV file. The file should have a header row and an index column. Numerical columns will be automatically detected for analysis.

            ### Data Exploration
            The dashboard provides several ways to explore your data:
            - **Show Data**: Displays the full dataset with row and column counts
            - **Show Summary**: Provides descriptive statistics for each numeric column
            - **Show Data Types**: Lists the data type of each column
            - **Show Missing Values**: Shows the count and percentage of missing values per column

            ### Visualisation Options
            #### Correlation Analysis
            - Generate an interactive correlation matrix of all numeric columns
            - Uses a red-blue color scale to indicate negative and positive correlations, respectfully
            - Hover over cells to see exact correlation values

            #### Distribution Analysis
            - Select any column from the dropdown menu to view its distribution
            - Histogram automatically adjusts bins based on data
            - Hover over bars to see frequency counts

            #### Bar Charts
            - Choose any column to create a bar chart
            - Useful for comparing values across samples, categories or time periods
            - Interactive tooltips show exact values

            #### Scatter Plots
            - Select different columns for X and Y axes
            - Useful for identifying relationships between variables
            - Zoom and pan to explore specific regions

            #### Exporting Visualisations
            All plots can be exported as PNG files:
            - Hover over any plot
            - Click the camera icon in the top-right corner
            - Choose save location on your computer

            ### Tips for Best Results
            - Ensure CSV files are properly formatted with headers
            - Numeric data should be clean and consistent
            - Large datasets may take longer to process
            """
        )
    
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
    """
    <a href='https://ko-fi.com/jordanprice' target='_blank'><img height='36' style='border:0px;height:36px;' 
    src='https://storage.ko-fi.com/cdn/kofi5.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>        
    """,
        unsafe_allow_html=True,
    )

# Title and description
st.title("📊 EDA Dashboard")
st.markdown("""
            <p style="font-size:1.3rem">
            Interactive dashboard for rapid exploratory data analysis (EDA) and 
            visualisation of tabular numerical data.</p>
            """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Custom CSS to improve appearance
st.markdown("""
    <style>
    .stButton>button {
        width: 80%;
        margin: 0 10%; 
    }
    </style>
""", unsafe_allow_html=True)

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

st.markdown("<br>", unsafe_allow_html=True)

# View data
st.write("## View Data and Summary Metrics")

col1, col2, col3, col4 = st.columns(4, gap="small")
show_data = col1.button("Show Data")
show_summary = col2.button("Show Summary")
show_types = col3.button("Show Data Types")
show_missing = col4.button("Show Missing Values")

# Display data based on button clicks
if show_data:
    st.dataframe(data, use_container_width=True)
    col1, col2  = st.columns(2)
    col1.metric(label="No. of Rows", value=f"{data.shape[0]:,.0f}")
    col2.metric(label="No. of Columns", value=f"{data.shape[1]:,.0f}")

if show_summary:
    st.dataframe(data.describe(), use_container_width=True)

if show_types:
    data_types = pd.DataFrame({
        'Data Types': data.dtypes
    })
    st.dataframe(data_types, use_container_width=True)

if show_missing:
    missing_df = pd.DataFrame({
        'Missing Values': data.isna().sum(),
        'Percentage': (data.isna().sum() / len(data) * 100).round(2)
    })
    st.dataframe(missing_df, use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)
st.write("## Visualise Data")

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs(["Correlation Analysis", "Distribution Analysis", "Bar Charts", "Scatter Plots"])

####### Correlation #######
with tab1:
    st.write("### Correlation Analysis")
    if st.button("Generate Correlation Matrix"):
        corr_matrix = data.select_dtypes(exclude='object').corr()
        fig = px.imshow(
            corr_matrix,
            color_continuous_scale='RdBu',
            aspect='auto',
            title='Correlation Matrix'
        )
        st.plotly_chart(fig, use_container_width=True)

####### Histogram #######
with tab2:
    st.write("### Distribution Analysis")
    hist_column = st.selectbox("Select variable for histogram:", headers)
    fig = px.histogram(
        data,
        x=hist_column,
        title=f'Distribution of {hist_column}',
        template='seaborn'
    )
    st.plotly_chart(fig, use_container_width=True)

####### Barchart #######
with tab3:
    st.write("### Bar Charts")
    bar_column = st.selectbox("Select variable for bar chart:", headers)
    fig = px.bar(
        data,
        y=bar_column,
        title=f'Bar Chart of {bar_column}',
        template='seaborn'
    )
    st.plotly_chart(fig, use_container_width=True)
    
####### Scatterplot #######
with tab4:
    st.write("### Scatter Plots")
    col1, col2 = st.columns(2)
    scatter_x = col1.selectbox("Select X-axis variable:", headers)
    scatter_y = col2.selectbox("Select Y-axis variable:", headers)
    fig = px.scatter(
        data,
        x=scatter_x,
        y=scatter_y,
        title=f'{scatter_y} vs {scatter_x}',
        template='seaborn'
    )
    st.plotly_chart(fig, use_container_width=True)


# Add footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center'>
    <a href='https://ko-fi.com/jordanprice' target='_blank'><img height='36' style='border:0px;height:36px;' 
    src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>  
    </p>      
    """,
    unsafe_allow_html=True,
)
st.markdown("<p style='text-align: center; color: grey;'>Copyright (c) 2025 <a href='https://rjprice.bio/' target='_blank'>Jordan Price</a>. Powered by Streamlit</p>", unsafe_allow_html=True)
