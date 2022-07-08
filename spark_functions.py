from termcolor import colored
class SparkQuerrying():
    def __init__(self,df,colInput):
        self.df = df
        self.colInput = colInput
    def SelectWhereGBy(self,whereCon,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).where(f'{whereCon}').groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(colored(e),'red')        
    def SelectGB(self,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(colored(e),'red') 
    def SelectWhere(self,whereCon):
        try:
            self.df.select(self.colInput).where(f'{whereCon}').show()
        except Exception as e:
            print(colored(e),'red') 
    def Select(self):
        try:
            self.df.select(self.colInput).show()
        except Exception as e:
            print(colored(e),'red')  


def columnGen(df):
    inputCol = []
    while True:
        print(colored("What would you like to do?", 'magenta'))
        print(colored("""\t1. Add more columns to you querry
\t2. To return to the main menu
        """,'cyan'))
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