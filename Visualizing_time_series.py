# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:02:59 2022

@author: arnab
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Natural_Data/Room3_WoodShop.csv', dtype={'Date':'str','Time':'str','Gasera':'double','Winsen1':'double','Winsen2':'int', 'SGP30':'double','Bosch1RH':'double','Bosh2RH':'double'})
df['Timestamp']= df['Date']+' '+df['Time']
df["Timestamp"] = df["Timestamp"].astype("datetime64")
df = df.set_index("Timestamp")


plt.plot(df["Gasera"], marker='o')

plt.xlabel("Timestamp")
plt.ylabel("Sensor reading formaldehyde")
plt.title("Gasera Time Series Plot")

plt.show()
