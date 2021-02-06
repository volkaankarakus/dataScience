# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 04:50:31 2021

@author: VolkanKarakuş
"""

#REVİEW of PANDAS
#As you notice, I do not give all idea in a same time. Although, we learn some basics of pandas, we will go deeper in pandas.

#single column = series
#NaN = not a number
#dataframe.values = numpy

#dictionary'dan dataFrame yaratmayi ve csv dosyasindan dataFrame yaratmayi gormustuk.
#3.YOL
#BUILDING DATA FRAMES FROM SCRATCH
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


country=['Spain','France']
population=['11','12']
listLabel=['country','population']
listCol=[country,population]
zipped=list(zip(listLabel,listCol))
dataDict=dict(zipped)
dataFrame=pd.DataFrame(dataDict)

#BROADCASTING(Create New Column)
dataFrame['capital']=['madrid','paris']
dataFrame['income']=0 #Broadcasting entire column

data=pd.read_csv('pokemon.csv')
data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()
# it is confusing
# subplots
data1.plot(subplots = True)
plt.show()

# hist plot  
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True) #norm yapinca frekanslari oran olarak verir.
# histogram subplot with non cumulative and cumulative
fig, axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[0])
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[1],cumulative = True)
plt.savefig('graph.png')
plt

#%% INDEXING PANDAS TIME SERIES
# Pandas'ta indexler time serie'lerden olusur.
# Bu yüzden time serilerle islemler yapilacak kaliplar gelistirilmis.
# yeni bir tur gorucez . string, int gibi : DATETIME
# datetime = object
# parse_dates(boolean): Transform date to ISO 8601 (yyyy-mm-dd hh:mm:ss ) format

#POKEMON DATASINDA TIMESERIE OLMADIGI ICIN TIMESERIE EKLEYELIM.

timeList = ["1992-03-08","1992-04-12"]
print(type(timeList[1])) #string
# however we want it to be datetime object
datetimeObject = pd.to_datetime(timeList)
print(type(datetimeObject)) # pandas.core.indexes.datetimes.DatetimeIndex

#  dataTimeIndex haline getirdik.

# In order to practice lets take head of pokemon data and add it a time list
data2 = data.head()
dateList = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetimeObject = pd.to_datetime(dateList)
data2["date"] = datetimeObject
# lets make date as index
data2= data2.set_index("date") #Index 0,1,2,3,4 yerine yeni indexim dataTimeObject(TimeSeries)

# Now we can select according to our date index
print(data2.loc["1993-03-16"]) #loc'a indexi yazip data okuyabiliyorduk, artık timeseries degerini yaziyoruz.
print(data2.loc["1992-03-10":"1993-03-16"]) # birden fazla data okuma.

# Resampling: statistical method over different time intervals
# Needs string to specify frequency like "M" = month or "A" = year

# We will use data2 that we create at previous part
meanYearly=data2.resample("A").mean() # yila göre resample et ve dataFramedeki herbir senenin kendi icinde ortalamasini al.
meanMonthly=data2.resample("M").mean()
#aylik mean alirken bazi aylar NaN kaldi.
#buraya Linear Interpolation yapilabilir . 1,2,3, ,5,6,7 (virgule 4 gelmesi gibi.)

interpolatedMeanMonthly=data2.resample("M").first().interpolate("linear") # stringler hala NaN kalir.


# Or we can interpolate with mean() #BOSLUKLARI ORTALAMAYA GORE DOLDURUR.
meanInterpolatedMeanMonthly=data2.resample("M").mean().interpolate("linear")

