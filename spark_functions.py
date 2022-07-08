class SparkQuerrying():
    def __init__(self,df,colInput):
        self.df = df
        self.colInput = colInput
    def SelectWhereGBy(self,whereCon,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).where(f'{whereCon}').groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(e)        
    def SelectGB(self,groupByVar,aggColnName,aggType):
        aggreagteDict = {k:v for (k,v) in zip(aggColnName, aggType)}
        try:
            self.df.select(self.colInput).groupby(f'{groupByVar}').agg(aggreagteDict).show()
        except Exception as e:
            print(e) 
    def SelectWhere(self,whereCon):
        try:
            self.df.select(self.colInput).where(f'{whereCon}').show()
        except Exception as e:
            print(e) 
    def Select(self):
        try:
            self.df.select(self.colInput).show()
        except Exception as e:
            print(e)  


def columnGen(df):
    inputCol = []
    while True:
        print("What would you like to do?")
        print("\t1. Add more columns to you querry")
        print("\t2. To return to the main menu")
        x = int(input("Please make a selection: "))

        if x == 1:
            print(f"The columns you can select are: {df.columns}")
            colInput = input("Please list the columns you would like: ") 
            inputCol.append(colInput)
        elif x == 2:
            break
        else:
            print("Please input a vaild number!")
    print(inputCol)
    return inputCol