import sys
from pyspark.sql.functions import to_timestamp, col, desc

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
from pyspark.sql import SparkSession, functions
from cassandra.cluster import Cluster
from data_clean_functions import clean_data
from data_filter_functions import filter_data, remove_null
from load_csv import read_csv

cluster_seeds = ['127.0.0.1']
spark = SparkSession.builder.appName('test').config('spark.cassandra.connection.host', ','.join(cluster_seeds))\
    .getOrCreate()
sc = spark.sparkContext

KEYSPACE = 'pirates'

def main(keyspace, inputs):

    crimes_dataset = read_csv()
    crimes_dataset = filter_data(crimes_dataset)
    crimes_dataset = clean_data(crimes_dataset)
    crimes_dataset = remove_null(crimes_dataset)

    crimes_dataset.show()
    crimes_dataset.printSchema()
    #crimes_dataset.write.format('csv').save('mycsv', header='true')

    """

    cluster = Cluster(['127.0.0.1'])

    session = cluster.connect()
    session.execute('CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = {\'class\' : \'SimpleStrategy\', \'replication_factor\' : 1}' %KEYSPACE)
    session.cluster.connect(keyspace=KEYSPACE)
    session.execute('CREATE TABLE IF not EXISTS  testcrime  (id INT, casenumber TEXT, block TEXT, iucr INT, crimetype TEXT, \
        description TEXT, location TEXT, arrest TEXT,  domestic TEXT, beat INT, district FLOAT, ward FLOAT, communityarea FLOAT, fbicode TEXT, \
        x_coordinate FLOAT, y_coordinate FLOAT, year INT, latitude FLOAT, longitude FLOAT, occurrence_date TIMESTAMP, updatedon TIMESTAMP, PRIMARY KEY (id, casenumber))')
    session.execute(' TRUNCATE testcrime')

    #crimes_dataset.write.format("org.apache.spark.sql.cassandra").options(table='testcrime', keyspace=keyspace).save()
    
    """
if __name__ == '__main__':
    inputs = 1
    keyspace = 1
    main(keyspace, inputs)