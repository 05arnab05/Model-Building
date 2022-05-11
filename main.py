from BlackBoxModels import Random_Forest
from WhiteboxModels import Lasso
import pandas as pd




def PreprocessingTS(data):
    data['timestamp']=pd.to_datetime(data['timestamp'])
    data['Conc']=data['Conc']*1000
    return data
   
def main():
   Concentration=pd.read_csv('https://raw.githubusercontent.com/05arnab05/Model-Building/main/Indoor%20Fromaldehyde%20sensing%20data/Concentration%20Only/Compiled_Comparative_Data_WithBosch.csv?token=GHSAT0AAAAAABSZJHLI6LK2Z5BNWPWVJOIYYR4PBZQ')
   Humidity=pd.read_csv('https://raw.githubusercontent.com/05arnab05/Model-Building/main/Indoor%20Fromaldehyde%20sensing%20data/Humidity%20only/Compiled_Comparative_Data_WithBosch.csv')
   Temperature=pd.read_csv('https://raw.githubusercontent.com/05arnab05/Model-Building/main/Indoor%20Fromaldehyde%20sensing%20data/Temperature%20only/Compiled_Comparative_Data_WithBosch.csv')
   Concentration= PreprocessingTS(Concentration)
   ob= Random_Forest(Concentration,"MinMax","TSDataSplit")
   ob.ModelTraining("SGP30","Conc")
   ob.ModelPrediction()
   
   


# =============================================================================
#    dataset = {"Concentration","Temperature","Humidity"}
#    for i in dataset:
#        a=Random_Forest(eval(i),"MinMax")
#        a.model()
#        
# =============================================================================
       

if __name__ == '__main__':
    
    main()
    
