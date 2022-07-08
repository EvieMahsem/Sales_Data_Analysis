from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import SparkQuerrying

spark = SparkSession.builder.getOrCreate()
data = pd.read_csv("csvGenerator/data.csv")
spark_df = spark.createDataFrame(data)


def insert_query():
    while True:
        print("This is the querying portion of the program.")
        lel = 0
        while lel != 5:
            print("\t1. To do a Where statment AND a Group By")
            print("\t2. To do a Where statment AND NO group By")
            print("\t3. To do a select statement with just a Group By") 
            print("\t4. A select statement without a where or group by")
            print("\t5. To return to the main menu")
            lel = int(input("Please make a selection: "))
            print("How many columns do you want to select?")
            print(f"The columns you can select are: {spark_df.columns}")
            colInput = input("Please list the columns you would like: ").split(',')
            obj = SparkQuerrying(spark_df,colInput) 
            aggreagteFunctions = ['count','max','min','first','last', 'mean','sum']
        
            if lel == 1:
                print(colInput)
                print("What is the conditional you would like to use? For example: orderID > 10 ")
                whereCon = input("Please input: ")
                print("What column do you want to group by?", colInput)
                groupByVar = input("Please input: ")
                keys = input("Please input the column names you want to aggregate: ").split(',')
                print(aggreagteFunctions)
                values = input("Please input the functions you would like to use: ").split(',')
                obj.SelectWhereGBy(whereCon,groupByVar,keys,values)
            elif lel == 2:
                print(colInput)
                print("What is the conditional you would like to use? For example: orderID > 10 ")
                whereCon = input("Please input: ")
                obj.SelectWhere(whereCon)                    
            elif lel == 3:
                print(colInput)
                print("What column do you want to group by?", colInput)
                groupByVar = input("Please input: ")
                keys = input("Please input the column names you want to aggreagte: ").split(',')
                print(aggreagteFunctions)
                values = input("Please input the functions you would like to use: ").split(',')
                obj.SelectGBy(groupByVar,keys,values)
            elif lel == 4:
                print(colInput)
                obj.Select(colInput)
            elif lel == 5:
                break
            else:
                print("Please make a valid input.")

def Startup ():
    while True:
        print("Hello, and welcome to the simulation.")
        print("\t1. ")
        print("\t2. To make a query.")
        print("\t3. To close out the program.")
        while True:
            try:
                sel = int(input("\nSelection: "))
            except (ValueError):
                print("ValueError")
                print("Please make a valid input.")
            else:
                break
        if sel == 1:
            pass
        elif sel == 2:
            insert_query()
        elif sel == 3:
            disfile = open('newFile.txt', 'w')
            disfile.write(' ')
            disfile.close()
            print("Alright, catch ya later then.")
            break
        else:
            print("Make a valid input.")

Startup()