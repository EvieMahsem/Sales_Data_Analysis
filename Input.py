from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import *
import graphGUI
from termcolor import colored

spark = SparkSession.builder.getOrCreate()
spark_df = spark.read.option('header', 'true').csv("csvGenerator/data.csv")



def insert_query():
    colInput = columnGen(spark_df)
    obj = SparkQuerrying(spark_df,colInput)
    while True:
        print(colored("What would you like to do?", 'magenta'))
        print(colored("""\t1. To do a Where statment AND a Group By
\t2. To do a Where statment AND NO group By
\t3. To do a select statement with just a Group By        
\t4. A select statement without a where or group by        
\t5. To return to the main menu        
        """,'cyan'))
        lel = int(input(colored("Please make a selection: ",'magenta')))
        if lel == 5:
            break

        if lel == 1:
            aggreagteFunctions = ['count','max','min','first','last', 'mean','sum']
            print(colored(colInput,'yellow'))
            print(colored("What is the conditional you would like to use? For example: orderID > 10 ",'cyan'))
            whereCon = input(colored("Please input: ",'magenta'))
            print(colored("What column do you want to group by?", "magenta"), colored(colInput,'yellow'))
            groupByVar = input(colored("Please input: ",'magenta'))
            keys = input(colored("Please input the column names you want to aggregate: ",'magenta')).split(',')
            print(colored(aggreagteFunctions,'yellow'))
            values = input(colored("Please input the functions you would like to use: ",'magenta')).split(',')
            obj.SelectWhereGBy(whereCon,groupByVar,keys,values)
        elif lel == 2:
            print(colored(colInput,'yellow'))
            print(colored("What is the conditional you would like to use? For example: orderID > 10 ",'cyan'))
            whereCon = input(colored("Please input: ",'magenta'))
            obj.SelectWhere(whereCon)                    
        elif lel == 3:
            aggreagteFunctions = ['count','max','min','first','last', 'mean','sum']
            print(colored(colInput,'yellow'))
            print(colored("What column do you want to group by?", "magenta"), colored(colInput,'yellow'))
            groupByVar = input(colored("Please input: ",'magenta'))
            keys = input(colored("Please input the column names you want to aggregate: ",'magenta')).split(',')
            print(colored(aggreagteFunctions,'yellow'))
            values = input(colored("Please input the functions you would like to use: ",'magenta')).split(',')
            obj.SelectGBy(groupByVar,keys,values)
        elif lel == 4:
            print(colored(colInput,'yellow'))
            obj.Select()
        else:
            print(colored("Please input a vaild number!",'red'))

def Startup ():
    while True:
        print(colored("Hello, and welcome to the simulation.", 'magenta'))
        print(colored("""\t1. To open visualization menu.
\t2. To make a query.
\t3. To close out the program.       
        """,'cyan'))
        while True:
            try:
                sel = int(input(colored("Selection: ",'magenta')))
            except (ValueError):
                print(colored("ValueError",'red'))
                print(colored("Please make a valid input.",'red'))
            else:
                break
        if sel == 1:
            graphGUI.startWindow()
        elif sel == 2:
            insert_query()
        elif sel == 3:
            print("Alright, catch ya later then.")
            break
        else:
            print("Make a valid input.")

Startup()