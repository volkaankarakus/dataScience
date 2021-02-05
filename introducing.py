# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:21:53 2021

@author: VolkanKarakuş
"""

import numpy as np                #linear algebra
import pandas as pd               #data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt   
import seaborn as sns             #visualization tool


data=pd.read_csv('pokemon.csv')
#data.info()
#%%
#correlation map 
#feature'lar arasindaki iliskiyi anlamamizi saglayan methodlardan biri.
#eger 2 feature arasi correlation 1'se dogru orantilidir diyebiliriz.
#    (evin oda sayisi ve fiyati gibi.)
#    (evin sehir merkezine uzakligi ve fiyati ters orantili. Negatif correlation )
#     (0'sa bir iliski yok.)


correlation=data.corr()
f,ax=plt.subplots(figsize=(13,13))
sns.heatmap(data.corr(),annot=True,linewidths=.5,fmt='.1f',ax=ax) #annot=True oranlarin tabloda gozukmesi.
plt.show()                                                        #linewidth, kareler arasi bosluk kalinligi

#data.head(10) , default degeri ilk 5 pokemonu verir.
                #genel yapiya bakmak icin .head() uygundur.

columns=data.columns
#%%
#MATPLOTLIB
# x axis eger zamansa, Line Plot 
# iki feature correlation'a bakmak, kiyaslamak icin Scatter Plot
# feature'in dagilimina bakmak istiyorsak Histogram.

data.Speed.plot(kind='line',color='g',label='Speed',linewidth=1,alpha=0.5,grid=True,linestyle=':')
data.Defense.plot(color='r',label='Defense',linewidth=1,alpha=0.5,grid=True,linestyle='-')
plt.legend(loc='upper right') # legend, labelleri koymamiza yarar.
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line Plot')

#%% SCATTER PLOT
# x=Attack, y=Defense
# scatterda karsilastirma yapildigi icin data.speed.plot gibi degil, parametre olarak icine yaziyoruz.

data.plot(kind='scatter',x='Attack',y='Defense',alpha=0.5,color='red')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack Defense Scatter Plot')

#%% HISTOGRAM
# bins, number of bar in Figure
data.Speed.plot(kind='hist',bins=50,figsize=(15,15))
plt.show()





