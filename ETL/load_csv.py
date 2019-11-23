from pyspark.sql import SparkSession
from db_architecture import crime_schema

spark = SparkSession.builder.appName('CC').getOrCreate()


def read_csv():
    # header set to true, else it will read the header line as null
    crimes_dataset = spark.read.format('csv').load('../Project/datafile/chicagocrime.csv',schema=crime_schema, header = True)
    print('dataset loaded')
    return crimes_dataset