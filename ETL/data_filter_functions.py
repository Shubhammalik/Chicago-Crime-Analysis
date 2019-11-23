from pyspark.sql.functions import to_timestamp, col, hour, substring
from pyspark.sql.types import IntegerType



def filter_data(df):
    columns_to_drop = ['iucr', 'beat', 'date1', \
                       'district', 'ward', 'domestic', \
                       'communityarea', 'fbicode', \
                       'updatedon', 'location']
    df = str_to_date(df)
    df = add_hour_column(df)
    df = add_am_pm_column(df)
    df = df.drop(*columns_to_drop)
    print('data filtered')
    return df


def str_to_date(df):
    df = df.withColumn('occurrence_date',to_timestamp(df.date1, 'MM/dd/yyyy HH:mm:ss'))\
        #.withColumn('updatedon',to_timestamp(df.updatedon1, 'MM/dd/yyyy HH:mm:ss'))
    return df

def add_hour_column(df):
    df = df.withColumn('hour', hour(df.occurrence_date).cast(IntegerType()))
    return df


def add_am_pm_column(df):
    df = df.withColumn('am_pm', substring('date1', 21, 2))
    return df

def remove_null(df):
    df = df.select('*').where(col('id').isNotNull() & col('casenumber').isNotNull())
    print('data check : unique')
    return df