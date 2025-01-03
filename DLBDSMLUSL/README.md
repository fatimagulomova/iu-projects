# Uncovering Patterns in Police Activity: A Data Science Approach to Equity

This project explores a large dataset of policing activities to uncover patterns and identify homogeneous categories of incidents. By applying unsupervised learning techniques, such as K-Means clustering, the project aims to reduce dataset complexity, provide meaningful visualizations, and support decision-making for equitable policing practices.

## Table of Contents
- Introduction
- Objectives
- Dataset
- Tech Stack
- Methodology
  - Data Collection and Preprocessing
  - Exploratory Data Analysis (EDA)
  - Cluster Analysis
- Results
- Usage
- Links
- Acknowledgements

## Introduction
This project leverages data science to address equity issues in policing by analyzing patterns in a dataset of police activities. The focus is on reducing data complexity, uncovering meaningful trends, and providing actionable insights through clustering and visualization.

## Objectives
- Understand the dataset structure and explore key variables.
- Reduce complexity through data preprocessing and feature engineering.
- Use K-Means clustering to group similar incidents.
- Provide visualizations and descriptive statistics to support equitable decision-making.

## Dataset
The dataset was sourced from Kaggle’s **Data Science for Good: Center for Policing Equity** and contains information on policing incidents from 2011 to 2015. After sampling and preprocessing, the dataset was reduced to **14,761 rows and 14 columns** for analysis.

## Tech Stack
- **Programming Language:** Python
- **Libraries:**
  - `pandas`, `numpy` for data manipulation and preprocessing
  - `matplotlib`, `seaborn` for data visualization
  - `scikit-learn` for clustering and imputation
  - `yellowbrick` for evaluating clustering models
  - `t-SNE` for dimensionality reduction and cluster visualization

## Methodology

### 1. Data Collection and Preprocessing
- Sampled a 10% subset of the original dataset for efficient analysis.
- Cleaned and imputed missing values, removed duplicates, and handled outliers.
- Extracted meaningful features such as `INCIDENT_YEAR` and `INCIDENT_MONTH`.
- Simplified street addresses and grouped rare categories for better clustering.

### 2. Exploratory Data Analysis (EDA)
- Explored distributions of offences by gender, location, and time.
- Visualized demographic trends and seasonal patterns using bar charts and heatmaps.

### 3. Cluster Analysis
- Applied K-Means clustering and identified the optimal number of clusters using the elbow method.
- Evaluated clustering results using metrics like Silhouette Score, Davies-Bouldin Index, and Calinski-Harabasz Index.
- Visualized clusters using t-SNE for interpretability.

## Results
- Identified 7 distinct clusters based on offender demographics, locations, and time of incidents.
- Key insights include demographic trends, high-crime locations, and seasonal patterns.
- The results provide a foundation for equitable policing practices and data-driven decision-making.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/fatimagulomova/policing-equity.git
