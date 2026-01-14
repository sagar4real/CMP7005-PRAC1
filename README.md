# 🇮🇳 India Air Quality Analytics & AQI Prediction  
CMP7005 – Programming for Data Analysis

## Project Overview
This project analyses air quality data across India to identify pollution trends, assess the impact of key atmospheric pollutants, and predict the Air Quality Index (AQI) using machine learning techniques. The work follows a complete data analytics and software development pipeline, including data handling, exploratory data analysis (EDA), predictive modelling, and application deployment.

An interactive Streamlit web application is developed to visualise air quality trends, identify highly polluted cities, and enable users to predict AQI values along with health-based recommendations.

## Objectives
- Analyse temporal and city-wise air quality trends across India  
- Identify key pollutants influencing AQI  
- Build and evaluate machine learning models for AQI prediction  
- Deploy an interactive application for AQI prediction and visual analytics  


## Dataset
**Source:** India Air Quality Dataset (CSV format provided via Moodle)

The dataset contains daily air quality measurements collected across multiple Indian cities.

**Key attributes include:**
- City, Date  
- Pollutant concentrations: PM2.5, PM10, NO2, SO2, CO, O3  
- Air Quality Index (AQI) and AQI category  

The dataset was cleaned and preprocessed to handle missing values, remove inconsistencies, and engineer time-based features such as year and month.

## Exploratory Data Analysis (EDA)
The EDA phase includes:
- Yearly and monthly AQI trend analysis  
- City-wise average AQI comparison  
- Distribution analysis of AQI and pollutant concentrations  
- Correlation analysis between pollutants and AQI  

Key insights highlight strong seasonal patterns and consistently higher pollution levels in major urban and industrial cities.

## Machine Learning Modelling
Two regression models were developed and evaluated:
- **Linear Regression** (baseline model)  
- **Random Forest Regressor** (advanced model)  

The Random Forest model demonstrated superior performance by effectively capturing non-linear relationships between pollutant concentrations and AQI.

Model performance was evaluated using:
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R-squared (R²) score  

## Application Development
A Streamlit-based web application was developed to demonstrate model deployment and user interaction. The application provides:
- AQI trend visualisations  
- City-wise air quality analysis  
- Interactive AQI prediction  
- AQI category classification  
- Health-based recommendations  

Due to Google Colab environment limitations, the application was executed in Colab and exposed using a tunnelling service for demonstration purposes.

## How to Run the Application

### Local Execution
1. Install required packages:
2. Navigate to the project directory.
3. Run:

### Google Colab Execution
- Install the required packages.
- Run the Streamlit app in the background.
- Expose the application using a tunnelling service such as **localtunnel** or **Cloudflare tunnel**.

## Results and Key Insights
- PM2.5 and PM10 are the strongest contributors to AQI.  
- AQI shows clear seasonal variation, with higher pollution levels during winter months.  
- The Random Forest model outperforms baseline models in AQI prediction accuracy.  

## Tools and Technologies
- Python  
- Pandas, NumPy  
- Matplotlib  
- Scikit-learn  
- Streamlit  
- Git and GitHub  

## Limitations and Future Work
The presence of missing values may affect prediction accuracy, and the model relies solely on historical data. Future improvements could include:
- Integration of real-time air quality data  
- Location-specific AQI prediction  
- Use of more interpretable or hybrid machine learning models  

## Author
**Student ID:** ST20318513  
**Module:** CMP7005 – Programming for Data Analysis  
**Academic Year:** 2025–2026  

## Acknowledgements
This project was completed as part of the CMP7005 coursework at Cardiff Metropolitan University. The dataset was provided for academic purposes, and all analysis was conducted in accordance with university guidelines.
