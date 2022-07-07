

class SparkQuerrying():
    def __init__(self,df,whereQ,groupQ,colInput):
        self.df = df
        self.whereQ = whereQ
        self.groupQ = groupQ
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



class DataAnalysis(SparkQuerrying):
    def __init__(self):
        pass
    def plotData(self):
        pass


