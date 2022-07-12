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
\t5. To return to the main menu""",'cyan'))
        lel = int(input(colored("Please make a selection: ",'magenta')))
        if lel == 5:
            break

        if lel == 1:

            #Start of Where code
            print(colored(colInput,'yellow'))
            print(colored("What column do you want to do a condition on? ",'cyan'))
            whereCol = input(colored("Please input: ",'magenta'))

            op = [">", "<", "="]
            print(colored(f"What type of opertator do you want to use: {colored(op,'yellow')}",'cyan'))
            whereOp = input(colored("Please input: ",'magenta'))

            print(colored("Please input the number or string of conditional:",'cyan'))
            whereValue = input(colored("Please input: ",'magenta'))
            #End of Where code

            #Start of GroupBy
            print(colored("What column do you want to group by?", "magenta"), colored(colInput,'yellow'))
            groupByVar = input(colored("Please input: ",'magenta'))
            #End of GroupBy
        
            #Start of agg (See Input.py for the function)
            aggCol, aggType = aggGen()
            #End of agg

            if whereOp == "<" or whereOp == ">":
                whereStatement = whereCol + " " + whereOp + " " + whereValue
                obj.SelectWhereGBy(whereStatement,groupByVar,aggCol,aggType)
            elif whereOp == "=":
                obj.SelectWhereGByEqual(whereCol,whereValue,groupByVar, aggCol, aggType)
            else:
                print(colored("Please enter a vaild opertator!",'red'))
            
        elif lel == 2:
            #Start of Where code
            print(colored(colInput,'yellow'))
            print(colored("What column do you want to do a condition on? ",'cyan'))
            whereCol = input(colored("Please input: ",'magenta'))

            op = [">", "<", "="]
            print(colored(f"What type of opertator do you want to use: {colored(op,'yellow')}",'cyan'))
            whereOp = input(colored("Please input: ",'magenta'))

            print(colored("Please input the number or string of conditional:",'cyan'))
            whereValue = input(colored("Please input: ",'magenta'))
            #End of Where code

            if whereOp == "<" or whereOp == ">":
                whereStatement = whereCol + " " + whereOp + " " + whereValue
                obj.SelectWhere(whereStatement)
            elif whereOp == "=":
                obj.SelectWhereEqual(whereCol, whereValue)
            else:
                print(colored("Please enter a vaild answer!",'red'))                  
        elif lel == 3:
            #Start of group by
            print(colored(colInput,'yellow'))
            print(colored("What column do you want to group by?", "magenta"), colored(colInput,'yellow'))
            groupByVar = input(colored("Please input: ",'magenta'))
            #End of group by

            #Start of agg (See Input.py for the function)
            aggCol, aggType = aggGen()
            #End of agg

            obj.SelectGB(groupByVar,aggCol,aggType)
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
\t3. To close out the program.""",'cyan'))
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