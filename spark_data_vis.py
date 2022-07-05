from pyspark.sql import SparkSession
import pandas as pd


#This builds the spark session 
spark = SparkSession.builder.getOrCreate()

# This is for taking a CSV as an input and returning a spark Dataframe
def dataFrameCreation(csvfile):

    data = pd.read_csv(f"{csvfile}")

    #All of this may not be needed, we will see once we have the data
    pandas_df = pd.DataFrame({
        'order_id': data['order_id'],
        'customer_id': data['customer_id'],
        'customer_name': data['customer_name'],
        'product_id': data['product_id'],
        'product_name': data['product_name'],
        'product_category': data['product_category'],
        'payment_type': data['payment_type'],
        'qty': data['qty'],
        'price': data['price'],
        'datetime': data['datetime'],
        'country': data['country'],
        'city':data['city'],
        'ecommerce_website_name':data['ecommerce_website_name'],
        'payment_txn_id': data['payment_txn_id'],
        'payment_txn_success': data['payment_txn_success'],
        'failure_reason':data['failure_reason']        
    })
    spark_df = spark.createDataFrame(pandas_df)
    return spark_df



def query():
    pass

def plot():
    pass

