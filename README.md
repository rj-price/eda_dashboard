# EDA Dashboard

### Overview
`eda_dashboard` is a Streamlit dashboard app for rapid exploratory data analysis (EDA) and visualisation of tabular numerical data in `.csv` format.

### Features
The app provides the following functionality:
- View data, summary statistics and number of missing values per column.
- Generate a correlation matrix and heatmap.
- Visualise data distributions as histograms.
- Plot selected column as bar chart.
- Determine pairwise relationships between specified columns via scatterplots.

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
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Run EDA Dashboard:
streamlit run eda_dashboard.py
```

## Dashboard Use
Set up initial dashboard using `assemblies.csv` containing genome assembly metrics.

Initial dashboard can plot barcharts or scatterplots based on any of the column headers, selected through the dropdown menus.

Include:
- How to download plots


<br>

---
---

<br>

## TO DO
### Features to add:
- PCA
- Clustering analysis
- Data editing?
