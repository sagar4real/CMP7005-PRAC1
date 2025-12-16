India Air Quality Analytics & AQI Prediction
CMP7005 – Programming for Data Analysis

Project Overview
This project analyses air quality data across India to identify pollution trends, evaluate the impact of key pollutants, and predict the Air Quality Index (AQI) using machine learning. The project follows a complete data analytics pipeline, including data handling, exploratory data analysis, predictive modelling, and application deployment.

An interactive Streamlit web application is developed to visualise air quality trends, identify highly polluted cities, and allow users to predict AQI values with health-based recommendations.

Objectives

Analyse temporal and city-wise air quality trends in India

Identify key pollutants influencing AQI

Build and evaluate machine learning models for AQI prediction

Deploy an interactive application for AQI prediction and visual analytics

Project Structure
CMP7005-PRAC1
data
--  india_air_quality_fully_cleaned.csv
models
--  aqi_random_forest_model.pkl
--  feature_names.pkl
app.py
notebook.ipynb
README.md

Dataset
Source: India Air Quality Dataset (CSV format provided via Moodle)
Key attributes include City, Date, pollutant concentrations (PM2.5, PM10, NO2, SO2, CO, O3), AQI, and AQI category.

The dataset was cleaned and preprocessed to handle missing values, remove inconsistencies, and engineer time-based features.

Exploratory Data Analysis (EDA)
The EDA phase includes yearly and monthly AQI trend analysis, city-wise average AQI comparison, distribution analysis of AQI and pollutant concentrations, and correlation analysis between pollutants and AQI.

Key insights highlight strong seasonal patterns and higher pollution levels in major urban and industrial cities.

Machine Learning Modelling
A baseline Linear Regression model and an advanced Random Forest Regressor were trained and evaluated. The Random Forest model demonstrated superior performance by capturing non-linear relationships between pollutant concentrations and AQI.

Model performance was evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared score.

Application Development
A Streamlit-based web application was developed to demonstrate model deployment and user interaction. The application provides AQI trend visualisations, city-wise air quality analysis, interactive AQI prediction, AQI category classification, and health-based recommendations.

Due to Google Colab limitations, the application was executed in Colab and exposed using a tunnelling service for demonstration purposes.

How to Run the Application
Local execution:
Install the required packages (streamlit, pandas, numpy, scikit-learn, joblib, matplotlib), navigate to the project directory, and run the Streamlit application using the command “streamlit run app.py”.

Google Colab execution:
Install the required packages, run the Streamlit app in the background, and expose it using ngrok or localtunnel.

Results and Insights
PM2.5 and PM10 are the strongest contributors to AQI.
AQI shows clear seasonal variation, with higher pollution levels during winter months.
The Random Forest model outperforms baseline models in AQI prediction accuracy.

Tools and Technologies
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Streamlit, Git, and GitHub.

Limitations and Future Work
The presence of missing values may affect prediction accuracy, and the model relies on historical data only. Future improvements could include real-time data integration, location-specific predictions, and the use of more interpretable models.

Author
Student ID: ST20318513
Module: CMP7005 – Programming for Data Analysis
Academic Year: 2025–26

Acknowledgements
This project was completed as part of the CMP7005 coursework. The dataset was provided for academic purposes, and all analysis was conducted in accordance with university guidelines.
