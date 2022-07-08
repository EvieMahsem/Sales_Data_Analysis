from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import SparkQuerrying


spark = SparkSession.builder.getOrCreate()
data = pd.read_csv("csvGenerator/data.csv")
spark_df = spark.createDataFrame(data)

def topSellingProductCountry(countryName):
    data = spark_df.select(['productName']).where(spark_df.country == countryName).groupBy('productName').agg({'productName': 'count'}).sort('count(productName)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingProductCity(cityName):
    data = spark_df.select(['productName']).where(spark_df.city == cityName).groupBy('productName').agg({'productName': 'count'}).sort('count(productName)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesPerCity():
    data = spark_df.select(['city']).groupBy('city').agg({'city': 'count'}).sort('count(city)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesPerCountry():
    data = spark_df.select(['country']).groupBy('country').agg({'country': 'count'}).sort('count(country)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalTopSelling():
    data = spark_df.select(['productCategory', 'quantity']).groupBy('productCategory').agg({'quantity': 'sum'}).sort('sum(quantity)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingCategoryCountry(countryName):
    data = spark_df.select(['productCategory', 'quantity']).where(spark_df.country == countryName).groupBy('productCategory').agg({'quantity': 'sum'}).sort('sum(quantity)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingCategoryCity(cityName):
    data = spark_df.select(['productCategory', 'quantity']).where(spark_df.city == cityName).groupBy('productCategory').agg({'quantity': 'sum'}).sort('sum(quantity)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList
    
def productPopYear(prodName):
    data = spark_df.select(['productName', 'datetime', 'quantity']).where(spark_df.productName == prodName).groupBy(spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('substring(datetime, 1, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productPopYearCountry(prodName, countryName):
    data = spark_df.select(['productName', 'datetime', 'country', 'quantity']).where((spark_df.productName == prodName) & (spark_df.country == countryName)).groupBy(spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('substring(datetime, 1, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productPopYearCity(prodName, cityName):
    data = spark_df.select(['productName', 'datetime', 'city', 'quantity']).where((spark_df.productName == prodName) & (spark_df.city == cityName) & (spark_df.quantity < 20000)).groupBy(spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('substring(datetime, 1, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList


