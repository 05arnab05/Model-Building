import pandas as pd
from abc import ABC,abstractmethod
from sklearn.ensemble import RandomForestRegressor
    
#Functions for Scaling data # take one array in and give out scaled 2 arrays
def MinMax(data):
    pass
    
    
#Functions for splitting data  #Take one array of time series in and give out two  
def SimpleSplit(data):
    timestamp = data['timestamp']
    train =''
    test= ''
    return train,test

def TimeSeriesSplit(data):
    timestamp = data['timestamp']
    train =''
    test= ''
    return train,test

def Kfold(data):
    timestamp = data['timestamp']
    train =''
    test= ''
    return train,test
    

#Dict for Data Splitting and Scaling functions
DataSplittingMethods = {
    'TSDataSplit': Sequence,
}
ScalingMethods = {
    'MinMax':MinMax
    
}


# Black box abstract class(Blueprint of a black box class)
class BlackBoxModel(ABC):

    @abstractmethod
    def DataSplit(self):
        pass
    
    @abstractmethod
    def Scaling(self):
        pass
    
    @abstractmethod
    def ModelTraining(self):
        pass
    
    @abstractmethod
    def ModelPrediction(self):
        pass

    
    @abstractmethod
    def PlotResults(self):
        pass
        
#black box classes, actual black box classes    
class Random_Forest(BlackBoxModel):
    
    def __init__(self,data,ScalingMethod,SplitMethod):
        #Create the test train split
        self.data=data
        self.ScalingMethod,self.SplitMethod=ScalingMethod,SplitMethod
        self.DataSplits={}
        self.Xlabel,self.Ylabel,self.model
    
    def DataSplit(self):
        TrainIndex,TestIndex=DataSplittingMethods[self.SplitMethod](self.data)
        self.DataSplits["train"]=self.data.iloc[TrainIndex,]
        self.DataSplits["test"]=self.data.iloc[TestIndex,]
        
    
    def Scaling(self,X,Y):
        ScaledX= ScalingMethods[self.ScalingMethod](X)
        ScaledY= ScalingMethods[self.ScalingMEthod](Y)
        return ScaledX,ScaledY
    
    
    def ModelTraining(self,Xlabel,Ylabel):
        self.Xlabel,self.Ylabel=Xlabel,Ylabel
        self.DataSplit()
        Xtrain= self.data.iloc[self.Xlabel]
        Ytrain= self.data.iloc[self.Ylabel]
        ScaledX,ScaledY= self.Scaling(Xtrain,Ytrain)
        self.Model=RandomForestRegressor(n_estimators=1000)
        self.Model.fit(ScaledX,ScaledY)
        
    
    def ModelPrediction(self):
        Xtest= self.DataSplits["test"].iloc[self.Xlabel]
        Ytest= self.DataSplits["test"].iloc[self.Ylabel]
        ScaledX,ScaledY= self.Scaling(Xtest,Ytest)
        self.Model.predict(Xtest)
        
    
    def PlotResults():
        pass
    

        
    
    


    
