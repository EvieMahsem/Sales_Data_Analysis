from pyspark.sql import SparkSession
import pandas as pd

#This builds the spark session 
spark = SparkSession.builder.getOrCreate()

data = pd.read_csv("csvGenerator/data.csv")
spark_df = spark.createDataFrame(data)
    
class SparkQuerrying():
    def __init__(self, df,whereQ,groupQ,colInput):
        self.df = df
        self.whereQ = whereQ
        self.groupQ = groupQ
        self.colInput = colInput
    def Select(self,df,whereQ,groupQ,colInput):
        aggreagteFunctions = ['count','max','min','first','last', 'mean','sum']

        if whereQ.lower() == 'no' and groupQ.lower() == 'yes':
            pass
        elif whereQ.lower() == 'yes' and groupQ.lower() == 'yes':
            print(colInput)
            print("What is the conditional you would like to use? For example: orderID > 10 ")
            whereCon = input("Please input: ")
            print("What column do you want to group by?", colInput)
            groupByVar = input("Please input: ")

            keys = input("Please input the column names you want to aggreagte: ").split(',')
            print(aggreagteFunctions)
            values = input("Please input the functions you would like to use: ").split(',')
            aggreagteDict = {k:v for (k,v) in zip(keys, values)}
            try:
                df.select(colInput).where(f'{whereCon}').groupby(f'{groupByVar}').agg(aggreagteDict).show()
            except:
                print("Please try again")

        elif whereQ.lower() == 'yes' and groupQ.lower() == 'no':
            pass
        elif whereQ.lower() == 'no' and groupQ.lower() == 'no':
            pass
        else:
            print("Please input a vaild input")





class DataAnalysis(SparkQuerrying):
    def __init__(self):
        pass
    def plotData(self):
        pass
    def close(self):
        pass



#Testing stuff
# print("How many columns do you want to select?")
# print(f"The columns you can select are: {df.columns}")
# colInput = input("Please list the columns you would like: ").split(',')

# whereQ = input("Would you like to add an conditional (yes/no): ")
# groupQ = input("Would you like to group data (yes/no): ")
# x = SparkQuerrying(spark_df).Select(spark_df,whereQ,groupQ,colInput)