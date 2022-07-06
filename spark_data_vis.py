from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import *

#This builds the spark session 
spark = SparkSession.builder.getOrCreate()

# This is for taking a CSV as an input and returning a spark Dataframe
def dataFrameCreation():
    data = pd.read_csv("csvGenerator/data.csv")
    spark_df = spark.createDataFrame(data)
    return spark_df
    

dataFrameCreation()


def queryOptions():
    pass
