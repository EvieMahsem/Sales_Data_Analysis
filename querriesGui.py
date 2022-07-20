from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import SparkQuerrying
import numpy as np


spark = SparkSession.builder.getOrCreate()
data = pd.read_csv("csvGenerator/data.csv")
# spark_df = spark.createDataFrame(data)
spark_df = spark.read.option('header', 'true').csv("csvGenerator/data.csv")

def topSellingProductCountry(countryName):
    data = spark_df.select(['productName', 'orderID']).where(spark_df.country == countryName).groupBy('productName').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingProductCity(cityName):
    data = spark_df.select(['productName', 'orderID']).where(spark_df.city == cityName).groupBy('productName').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesPerCity():
    data = spark_df.select(['city', 'orderID']).groupBy('city').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def compareTotalSalesPerCity(cityList):
    data = spark_df.select(['city', 'orderID']).where(spark_df.city.isin(cityList)).groupBy('city').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesPerCountry():
    data = spark_df.select(['country', 'orderID']).groupBy('country').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalTopSelling():
    data = spark_df.select(['productCategory', 'orderID']).groupBy('productCategory').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingCategoryCountry(countryName):
    data = spark_df.select(['productCategory', 'orderID']).where(spark_df.country == countryName).groupBy('productCategory').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingCategoryCity(cityName):
    data = spark_df.select(['productCategory', 'orderID']).where(spark_df.city == cityName).groupBy('productCategory').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList
    
def productPopYear(prodName):
    outlierTest = spark_df.select(['productName', 'quantity']).where(spark_df.productName.isin(prodName)).sort('quantity').collect()
    outlierData = [int(i[1]) for i in outlierTest]
    quart1, quart3 = np.quantile(outlierData, [0.25, 0.5, 0.75])[0], np.quantile(outlierData, [0.25, 0.5, 0.75])[2]
    # quart1, quart3 = 0, 10000

    info = {}
    for i in prodName:
        info[i] = []
    data = spark_df.select(['productName', 'datetime', 'quantity']).where((spark_df.productName.isin(prodName)) & (spark_df.quantity >= quart1) & (spark_df.quantity <= quart3)).groupBy(spark_df.productName, spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('productName', 'substring(datetime, 1, 2)').collect()
    spark_df.select(['productName', 'datetime', 'quantity']).where((spark_df.productName.isin(prodName)) & (spark_df.quantity >= quart1) & (spark_df.quantity <= quart3)).groupBy(spark_df.productName, spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('productName', 'substring(datetime, 1, 2)').show()
    for i in data:
        info[i[0]].append([str(i[1]), i[2]])

    return info

def productPopYearCountry(prodName, countryName):
    outlierTest = spark_df.select(['productName', 'quantity']).where((spark_df.productName.isin(prodName)) & (spark_df.country == countryName)).sort('quantity').collect()
    outlierData = [int(i[1]) for i in outlierTest]
    quart1, quart3 = np.quantile(outlierData, [0.25, 0.5, 0.75])[0], np.quantile(outlierData, [0.25, 0.5, 0.75])[2]

    data = spark_df.select(['productName', 'datetime', 'country', 'quantity']).where((spark_df.productName.isin(prodName)) & (spark_df.country == countryName) & (spark_df.quantity >= quart1) & (spark_df.quantity <= quart3)).groupBy(spark_df.productName, spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('productName', 'substring(datetime, 1, 2)').collect()
    info = {}
    for i in prodName:
        info[i] = []
    for i in data:
        info[i[0]].append([str(i[1]), i[2]])

    return info
def productPopYearCity(prodName, cityName):
    outlierTest = spark_df.select(['productName', 'quantity']).where((spark_df.productName.isin(prodName))).sort('quantity').collect()
    outlierData = [int(i[1]) for i in outlierTest]
    quart1, quart3 = np.quantile(outlierData, [0.25, 0.5, 0.75])[0], np.quantile(outlierData, [0.25, 0.5, 0.75])[2]


    data = spark_df.select(['productName', 'datetime', 'city', 'quantity']).where((spark_df.productName.isin(prodName)) & (spark_df.city == cityName) & (spark_df.quantity >= quart1) & (spark_df.quantity <= quart3)).groupBy(spark_df.productName, spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('productName', 'substring(datetime, 1, 2)').collect()
    info = {}
    for i in prodName:
        info[i] = []
    for i in data:
        info[i[0]].append([str(i[1]), i[2]])

    return info

def totalSalesTime():
    data = spark_df.select(['orderID', 'datetime']).groupBy(spark_df.datetime.substr(12,2)).agg({'orderID': 'count'}).sort('substring(datetime, 12, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productSalesTime(product):
    data = spark_df.select(['productName', 'orderID', 'datetime']).where(spark_df.productName.isin(product)).groupBy(spark_df.productName, spark_df.datetime.substr(12,2)).agg({'orderID': 'count'}).sort('productName', 'substring(datetime, 12, 2)').collect()
    spark_df.select(['productName', 'datetime']).where(spark_df.productName.isin(product)).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').show()

    info = {}
    for i in product:
        info[i] = []
    for i in data:
        info[i[0]].append([str(i[1]), i[2]])

    return info

def productSalesTimeCountry(product, country):
    data = spark_df.select(['productName', 'datetime']).where((spark_df.productName.isin(product)) & (spark_df.country == country)).groupBy(spark_df.productName, spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('productName', 'substring(datetime, 12, 2)').collect()
    spark_df.select(['productName', 'datetime']).where((spark_df.productName.isin(product)) & (spark_df.country == country)).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').show()
    info = {}
    for i in product:
        info[i] = []
    for i in data:
        info[i[0]].append([str(i[1]), i[2]])

    return info

def productSalesTimeCity(product, city):
    data = spark_df.select(['productName', 'orderID', 'datetime']).where((spark_df.productName.isin(product)) & (spark_df.city == city)).groupBy(spark_df.productName, spark_df.datetime.substr(12,2)).agg({'orderID': 'count'}).sort('productName', 'substring(datetime, 12, 2)').collect()
    spark_df.select(['productName', 'datetime']).where((spark_df.productName.isin(product)) & (spark_df.city == city)).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').show()
    info = {}
    for i in product:
        info[i] = []
    for i in data:
        info[i[0]].append([str(i[1]), i[2]])

    return info


