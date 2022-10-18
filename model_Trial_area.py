# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:40:26 2022

@author: arnab
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import BaggingRegressor

from sklearn import tree
from sklearn.tree import export_text


#Loading dataset
df = pd.read_csv('Controlled_Env_Data/Concentration Only/Compiled_Comparative_Data_WithBosch.csv')
features = ['Temperature','Humidity','SGP30']
df['Conc']=df['Conc']*1000
Xtrain = df.loc[0:8000, features]

Ytrain = df.loc[0:8000, 'Conc'].values

Xtest= df.loc[9001:11669, features]

Ytest=df.loc[9001:11669, 'Conc'].values



reg = RandomForestRegressor(n_estimators=200,max_depth=None,min_samples_split=2, max_features= 0.3, random_state = 0,oob_score = True,bootstrap=True)

reg.fit(Xtrain, Ytrain)

print('OOB score is:',reg.oob_score_*100, '%')

score = reg.score(Xtest, Ytest)
print('Testing score is',score*100, '%')

importances = pd.DataFrame({'feature':Xtrain.columns,'importance':np.round(reg.feature_importances_,3)})
importances = importances.sort_values('importance',ascending=False)

print(importances)