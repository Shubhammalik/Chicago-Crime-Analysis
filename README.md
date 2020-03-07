# Chicago Crime Analysis - Big Data

Goal for this project is to analyze chicago crime data from 2001-2018.

Dataset - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2

This dataset contained records from 2001 - 2018. Size - 1.6GB data (6.6M unique records).

# Coverage and Modules insights
1) ETL (Cleaning and Filtering) and Data operations (child tables creation and write to Cassandra DB).
2) Interactive visualizations for Hourly, Monthly and Yearly Crime Analysis (Line Charts and GEO maps).
3) Wordcloud implementation for most occuring crime type and crime location.
4) Time series Forecasting of crime for 2019.
5) Static visualizations for crime severity, Successful arrests (area-wise).
6) Predctive analysis of severity of crime based on arrest and crime type.

# Tech Stack
1) Data Cleaning & Filtering - Spark Dataframes and Spark SQL functions
2) Data Manipulation - Spark, Cassandra, Python, Pandas
3) Data Visualization - Plotly, Seaborn, Matplotlib, word cloud, Dash
4) Data Storage - Cassandra db
5) Forecasting - FBprophet
6) Webapp - Dash, Flask

# Running Instructions and Details
1) Details and findings of the project can be found in the report
2) Running instructions can be found inside RUNNING.md
3) For running application, go to the directory where app.py is present and run the below command:
    `spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 app.py`
    
# Illustration from Webapp
![Interactive tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_interactive_tab.png)

![Forecast tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_forecast_tab.png)

![Static tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_static_tab.png)

![Word cloud tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_wordcloud_tab.png)
