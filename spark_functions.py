from termcolor import colored
from pyspark.sql.functions import col

class SparkQuerrying():
    def __init__(self,df,colInput):
        self.df = df
        self.colInput = colInput
    
    def SelectWhereGBy(self,whereCon,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).where(f'{whereCon}').groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(colored(e,'red'))
    
    def SelectWhereGByEqual(self,whereCol,whereValue,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).where(col(whereCol) == f'{whereValue}').groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(colored(e,'red'))    
    
    def SelectGB(self,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(colored(e,'red'))
    
    def SelectWhere(self,whereCon):
        try:
            self.df.select(self.colInput).where(f'{whereCon}').show()
        except Exception as e:
            print(colored(e,'red'))
    
    def SelectWhereEqual(self,whereCol, whereValue):
        try:
            self.df.select(self.colInput).where(col(whereCol) == f'{whereValue}').show()
        except Exception as e:
            print(colored(e,'red'))
    
    def Select(self):
        try:
            self.df.select(self.colInput).show()
        except Exception as e:
           print(colored(e,'red'))
 



def columnGen(df):
    inputCol = []
    while True:
        print(colored("What would you like to do?", 'magenta'))
        print(colored("""\t1. Add more columns to you querry
\t2. To return to the main menu""",'cyan'))
        x = input(colored("Please make a selection: ", 'magenta'))
        if x == "1":
            print(colored(f"The columns you can select are: {colored(df.columns,'yellow')}",'cyan'))
            colInput = input(colored("Please list the columns you would like: ",'magenta')) 
            inputCol.append(colInput)
        elif x == "2":
            break
        else:
            print(colored("Please input a vaild number!",'red'))
    return inputCol



def aggGen():
    aggType = []
    aggCol = []
    while True:
        print(colored("What would you like to do?", 'magenta'))
        print(colored("""\t1. Add more aggregates?
\t2. To return to the main menu """,'cyan'))
        x = input(colored("Please make a selection: ", 'magenta'))
        if x == "1":
            aggColQ = input(colored("Please input the name of the column you would like to aggregate: ",'magenta'))
            aggCol.append(aggColQ )

            aggreagteFunctions = {'1':'count', '2':'max', '3':'min', '4':'first', '5':'last', '6':'mean', '7':'sum'}
            print(colored("What would you like to do?", 'magenta'))
            print(colored("""\t1. count
\t2. max
\t3. min      
\t4. first        
\t5. last 
\t6. mean
\t7. sum""",'cyan'))
            key = input(colored("Please make a selection: ",'magenta'))
            if key in ['1','2','3','4','5','6','7']:           
                aggType.append(aggreagteFunctions[key])
        elif x == "2":
            break
        else:
            print(colored("Please input a vaild number!",'red'))

    return aggCol, aggType