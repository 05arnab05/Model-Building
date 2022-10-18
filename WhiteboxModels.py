import pandas as pd
from numpy import arange
from sklearn.linear_model import LassoCV
from sklearn.model_selection import RepeatedKFold,cross_val_score

from abc import ABC,abstractmethod

def PreprocessingTS(data):
        data['timestamp']=pd.to_datetime(data['timestamp'])
        data['Conc']=data['Conc']*1000
        return data

def ScalingData(data, Scaling):
    Scaling(data)
    
def DataSplit():
    pass

#Dict for Data Splitting and Scaling functions
DataSplittingMethods = {
    'TSDataSplit': Sequence,
}
ScalingMethods = {
    'MinMax':MinMax
    
}

class WhiteBoxModel(ABC):
    
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
        
    
class LassoModel(WhiteBoxModel):
    
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
        cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1) # define model evaluation method
        self.Model= LassoCV(alphas=arange(0, 1, 0.01), cv=cv, n_jobs=-1) # define model
        self.Model.fit(ScaledX,ScaledY)
        
    
    def ModelPrediction(self):
        Xtest= self.DataSplits["test"].iloc[self.Xlabel]
        Ytest= self.DataSplits["test"].iloc[self.Ylabel]
        ScaledX,ScaledY= self.Scaling(Xtest,Ytest)
        self.Model.predict(Xtest)
        cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
        scores= cross_val_score(self.Model, ScaledX, ScaledY, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
        return scores
    
    def PlotResults(self):
        pass
    

class IAP(WhiteBoxModel): # Alan's testing zone
    
    def __init__(self,data,Scaling):
        self.data= data.PreprocessingTS(data)
        self.ScaledData= ScalingData(self.data, Scaling)
        
    def Model(self):
        pass
    
    def Predict():
        pass
    
    def Plot():
        pass
