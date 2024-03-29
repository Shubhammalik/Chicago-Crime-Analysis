import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql.functions import col
from pyspark.sql import SparkSession, functions


cluster_seeds = ['127.0.0.1']
spark = SparkSession.builder.appName('Crime Area Analysis').config('spark.cassandra.connection.host', ','.join(cluster_seeds)).getOrCreate()
spark.sparkContext.setLogLevel('WARN')
sc = spark.sparkContext

KEYSPACE ='pirates'
table_names = ['district_arrest','ward_arrest','communityarea_arrest']

#Area-wise Crime analysis {Ward, District, CommunityArea}
def crime_area_analysis(KEYSPACE):
    for table in table_names:

        level = table.split('_')[0]
        df = spark.read.format("org.apache.spark.sql.cassandra").options(table='{}_arrest'.format(level), keyspace=KEYSPACE).load()
        arrest_success = df.filter(col('arrest') == True).sort(level)
        arrest_true_count = list(arrest_success.select('count').toPandas()['count'])
        data = df.groupby(level).agg(functions.sum(df['count']).alias('count')).sort(level)
        x_labels = list(data.select(level).toPandas()[level])
        total_crime = list(data.select('count').toPandas()['count'])

        ind = np.arange(len(x_labels))
        width = 0.35

        p1 = plt.bar(ind, arrest_true_count, width)
        p2 = plt.bar(ind, total_crime, width, bottom=arrest_true_count)

        plt.ylabel('Count')
        plt.title('Arrest vs Total Crime - {} Data'.format(level.capitalize()))
        plt.xticks(ind, x_labels, rotation='vertical')
        plt.legend(['Arrests', 'Total Crime'])
        plt.savefig('./static/images/{}_static.png'.format(level))
        arrest_true_count.clear()
        x_labels.clear()
        total_crime.clear()




#crime_area_analysis()
"""
Function being called in app.py

# Command to run the file individually (makes connection to cassandra database)
uncomment the command above and run using the command below (provided dependencies are met)

spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 area_arrests/area_analysis.py

"""