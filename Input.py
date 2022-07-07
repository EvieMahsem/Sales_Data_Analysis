from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import SparkQuerrying

def insert_query():
    while True:
        print("This is the querying portion of the program.")
        print("\t1. Do a Where statment AND a Group By")
        print("\t2. Do a Where statment AND NO group By")
        print("\t3. Do just a Group By") 
        print("\t4. Just the normal select statment")
        print("\t5. To return to the main menu")
        lel = int(input("Please make a selection: "))
        while lel != 5:
            if lel == 1:
                print(lel)
            elif lel == 5:
                break

def Startup ():
    while True:
        print("Hello!")
        print("\t1. ")
        print("\t2. To make a query.")
        print("\t3. Stuff")
        print("\t4. To close out the program.")
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
        elif sel==3:
            pass
        elif sel == 4:
            disfile = open('newFile.txt', 'w')
            disfile.write(' ')
            disfile.close()
            print("Alright, catch ya later then.")
            break

Startup()