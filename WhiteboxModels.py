import pandas as pd
from abc import ABC,abstractmethod

def PreprocessingTS(data):
        data['timestamp']=pd.to_datetime(data['timestamp'])
        data['Conc']=data['Conc']*1000
        return data

def ScalingData(data, Scaling):
    Scaling(data)
    
def DataSplit():
    pass


class WhiteBoxModel(ABC):
    
    @abstractmethod
    def Model(self):
        pass
    
    @abstractmethod
    def Predict(self):
        pass
    
    @abstractmethod
    def Plot(self):
        pass
        
    
class Lasso(WhiteBoxModel):
    
    def __init__(self,data,Scaling):
        self.data= data.PreprocessingTS(data)
        self.ScaledData= ScalingData(self.data, Scaling)
        
    def Model(self):
        pass
    
    def Predict():
        pass
    
    def Plot():
        pass
    

        
        
    
    

        
    
    

    

    
