# EDA Dashboard

### Overview
`eda_dashboard` is a Streamlit dashboard app for rapid exploratory data analysis (EDA) and visualisation of tabular data in `.csv` format.

### Features
The app provides the following functionality:
- Upload and analyse custom CSV files with automatic data type detection
- View data, summary statistics and number of missing values per column
- Generate a correlation matrix and heatmap
- Visualise data distributions as histograms
- Plot a selected column as a bar chart
- Determine pairwise relationships between specified columns via scatterplots
- Interactive plots with zoom, pan, and hover capabilities
- Export visualisations as PNG files

<br>

## Getting Started

### Requirements
The following software packages must be installed prior to running (please refer to the linked installation instructions for your operating system):
- [Git](https://github.com/git-guides/install-git)
- [Python](https://www.python.org/downloads/)

### Installation
After installing Git and Python, install the app as follows:
```bash
# Get app from GitHub
git clone https://github.com/rj-price/eda_dashboard.git 

# Change into directory
cd eda_dashboard

# Create Python virtual environment 
python -m venv venv

# Activate environment
source venv/bin/activate        # On Windows use: venv\Scripts\activate

# Install required Python packages
pip install -r requirements.txt

# Run EDA Dashboard:
streamlit run eda_dashboard.py
```

<br>

## Dashboard Use
### Data Upload
The dashboard initially loads with example data (`assemblies.csv`) containing genome assembly metrics.

To analyze your own data, click the "Upload your CSV file" button and select any CSV file. The file should have a header row and an index column. Numerical columns will be automatically detected for analysis.

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

#### Heatmap
- Select multiple columns to visualise their relationships
- Adjust color scale intensity using the slider (*coming soon*)
- Hover over bars for index and value

#### Exporting Visualisations
All plots can be exported as PNG files:
- Hover over any plot
- Click the camera icon in the top-right corner
- Choose save location on your computer

### Tips for Best Results
- Ensure CSV files are properly formatted with headers
- Numeric data should be clean and consistent
- Large datasets may take longer to process
- For optimal visualisation, limit heatmap selection to related variables

<br>

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or feedback, please open an issue on GitHub.

<br>

<br>

---
---

<br>

## TO DO
### Features to add:
- PCA
- Clustering analysis
- Data editing?
