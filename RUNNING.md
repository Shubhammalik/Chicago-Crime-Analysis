1. Get Dataset

    Download dataset from the below link and save it in your own created datafile folder

    `https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2`

2. If you are running it for the first time then uncomment the following lines in the app.py

    a. generate_master_tables(format='cassandra', truncate='no', drop_table='no')
    
    b. generate_tables(format='cassandra')
    
    c. generate_wordcloud()
    
    d. severity_deduction(KEYSPACE='pirates')
    
    e. arrest_history()
    
    f. ward_analysis()
    
    g. district_analysis()
    
    h. communityarea_analysis()
    
    i. crime_forecasting()

    After uncommenting the codes, run the following command:

        spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 app.py

3. After running app.py for the first time, comment the above codes. To run app.py next time, simply type the spark-submit command.



