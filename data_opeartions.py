import sys

from pyspark.sql.functions import desc, hour, substring, col
from pyspark.sql.types import IntegerType

assert sys.version_info >= (3, 5)
from pyspark.sql import SparkSession, functions

spark = SparkSession.builder.appName('data operations').getOrCreate()
sc = spark.sparkContext

def main():
    data = spark.read.format('csv').load('../Project/datafile/mycsv/*.csv', header = True)
    #data.show()

    major_crimetypes = ['theft', 'battery', 'criminal_damage', 'narcotics', 'other_offense', \
                        'assault', 'burglary', 'motor_vehicle_theft', 'deceptive_practice', \
                        'robbery', 'criminal_trespass', 'weapons_violation', 'prostitution']

    #Major crimetype column addition
    data = data.select('*').withColumn('major_crime', data.crimetype.isin(major_crimetypes).astype('int'))\
        .where(col('hour').isNotNull())

    """
    #Hourly major crime
    hourly_major_crime = data.withColumn('hour_info', data.hour.cast(IntegerType()))
    hourly_major_crime = hourly_major_crime.select('id', 'hour_info', 'am_pm', 'major_crime','crimetype').where(col('major_crime')==1)
    hourly_major_crime = hourly_major_crime.select('id', 'hour_info', 'am_pm','crimetype').groupBy('hour_info', 'am_pm','crimetype')\
        .agg(functions.count(hourly_major_crime['id']).alias('count')).sort('am_pm', 'hour_info')
    hourly_major_crime.show(350, False)
    
    # Hourly Intensity of Crime
    #hourly_crime = data.select('id', 'hour', 'am_pm').where(col('hour').isNotNull())
    hourly_crime = data.withColumn('hour_info',data.hour.cast(IntegerType()))
    hourly_crime = hourly_crime.groupby('hour_info','am_pm').agg(functions.count(hourly_crime['id']).alias('count'))\
    .sort('am_pm', 'hour_info')
    hourly_crime.show(24,False)

    # Total Crimetype each year
    crimetype_yearly = data.select('id', 'year', 'crimetype')
    crimetype_yearly = crimetype_yearly.groupby('year','crimetype').agg(functions.count(crimetype_yearly['id'])\
    .alias('count')).sort('year',desc('count'))
    crimetype_yearly.show(1000, False)
    
    # Primary crime count
    crimetype = data.select('id', 'crimetype')
    crimetype = crimetype.groupby('crimetype').agg(functions.count(crimetype['id']).alias('count')).sort(desc('count'))
    crimetype.show(100, False)
    
    # All location's crime count
    location_crime = data.select('id', 'location_description')
    location_crime = location_crime.groupby('location_description').agg(functions.count(location_crime['id'])\
    .alias('count')).sort(
        desc('count'))
    location_crime.show(600, False)
    
    # Write the data to a csv file
    data.write.format('csv').save('mycsv', header='true')
    """


if __name__ == '__main__':
    main()