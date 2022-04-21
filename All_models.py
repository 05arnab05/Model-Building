import pandas as pd
Concentration=pd.read_csv('https://raw.githubusercontent.com/05arnab05/Model-Building/main/Indoor%20Fromaldehyde%20sensing%20data/Concentration%20Only/Compiled_Comparative_Data_WithBosch.csv?token=GHSAT0AAAAAABSZJHLI6LK2Z5BNWPWVJOIYYR4PBZQ')
Humidity=pd.read_csv('https://raw.githubusercontent.com/05arnab05/Model-Building/main/Indoor%20Fromaldehyde%20sensing%20data/Humidity%20only/Compiled_Comparative_Data_WithBosch.csv')
Temperature=pd.read_csv('https://raw.githubusercontent.com/05arnab05/Model-Building/main/Indoor%20Fromaldehyde%20sensing%20data/Temperature%20only/Compiled_Comparative_Data_WithBosch.csv')

def Preprocessing():
    global Concentration, Humidity, Temperature
    Datasets= {"Concentration","Humidity","Temperature"}
    for i in Datasets:
        eval(i)['timestamp']=pd.to_datetime(eval(i)['timestamp'])
        
    
def main():
    Preprocessing()
    
    
if __name__ == '__main__':
    main()