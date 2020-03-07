## Crime Dataset Analysis- City of Chicago (2001-2018)

Our goal for this project is to analyze chicago crime data from 2001-2018 and use interactive and static plots to analyse and understand the patterns in the crime. We also used crime forecasting to predict crime rate for the next one year and examine crime rate trends over the years, word-cloud to understand major occurring crimes and the most affected location type and geo Maps for plotting crime density of each crime on geo maps.


Illustrations from Webapp - 

https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_interactive_tab.png

https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_forecast_tab.png

https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_static_tab.png

https://github.com/Shubhammalik/Chicago-Crime-Analysis/blob/master/webapp_wordcloud_tab.png

**Extensive work has be done on** : ETL, Visualizations, Algorithmic Modules (Severity, Arrest, Forecasting)


Contributors:

    Shubham Malik
    Rohan Harode
    Akash Singh Kunwar
    
    


We have used the following Tech:

	1. Cassandra for NOSQL database management query`
	2. Dash Plotly for interactive analytics dashboard
	3. Plotly, Seaborn and matplotlib for static graphs
	4. Flask for backend 
	5. FB Prophet for forecasting

Dataset:
Dataset is available in the chicago data portal:
    `https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2`


The project is done as a part of SFU CMPT 732 Big Data coursework

   1. Details of the project can be found at submitted report
   2. Running instructions can be found inside RUNNING.md
   3. For running application, go to the directory where app.py is present and run the below command:
    `spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 app.py`