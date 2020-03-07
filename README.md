# Chicago-Crime-Analysis - Big Data
Analysis of Crimes committed in Chicago from 2001 to 2019

Dataset - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2

This dataset contained records from 2001 - 2019. Size - 1.6GB data (6.6M unique records).

# Analyses and Insights into Modules
1) ETL (Cleaning and Filtering) and Data preparation (child tables creation using Spark dataframe and write to Cassandra DB).
2) Interactive visualizations for Hourly, Monthly and Yearly Crime Analysis (Line Charts and GEO maps).
3) Wordcloud implementation for most occuring crime type and crime location.
4) Forecasting of crime for 2019.
5) Static visualizations for crime severity, successful arrests (area-wise).
6) Designed an interactive web app using Dash framework & Flask server for dynamic generation of plots (Time series and geo maps) and to present data findings 

# Tech Stack -
1) Data Cleaning & Filtering - Spark Dataframes and Spark SQL functions
2) Data Manipulation - Spark, Cassandra, Python, Pandas
3) Data Visualization - Plotly, Seaborn, Matplotlib, Word Cloud, Dash
4) Data Storage - Cassandra db
5) Forecasting - FBprophet
6) Webapp - Dash, Flask

# Running Instructions and details
The project is done as a part of SFU CMPT 732 Big Data coursework
1) Details of the project can be found in the report
2) Running instructions can be found inside RUNNING.md
3) For running application, go to the directory where app.py is present and run the below command:
    `spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 app.py`

# Illustrations from the web application
