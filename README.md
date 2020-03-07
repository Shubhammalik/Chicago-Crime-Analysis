# Chicago Crime Analysis - Big Data

Goal for this project is to analyze chicago crime data from 2001-2018.

[Dataset](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2) contains crime records from 2001 - 2018. Size - 1.6GB data (6.6M unique records).

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
1) Details and findings of the project can be found in the [report](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/Chicago_Crime_Analysis_Report.pdf)
2) Install the required libraries listed in [requirement.txt](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/requirements.txt)
3) Download the datastet from the chicago PD website [link](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2)
2) Running instructions can be found inside [RUNNING.md](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/RUNNING.md)
3) For running application, go to the directory where [app.py](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/app.py) is present and run the below command:

    `spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 app.py`
    
# Illustration from Webapp
**Interactive tab**
![Interactive tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/static/images/webapp_interactive_tab.png)

**Crime Forecasting**
![Forecast tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/static/images/webapp_forecast_tab.png)

**Static Visualizations**
![Static tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/static/images/webapp_static_tab.png)

**Word clouds**
![Word cloud tab](https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/static/images/webapp_wordcloud_tab.png)
