# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:11:17 2021

@author: VolkanKarakuş
"""

import pandas as pd

data=pd.read_csv('pokemon.csv')
data=data.set_index('#') #index 0'dan degil,1'den baslasin diye bunu yaptik.
headData=data.head()

#verilere erismenin birden fazla yolu vardi.
firstIndexHP1=data['HP'][1]
#ya da
firstIndexHP2=data.HP[1]
#ya da 
firstIndexHP3=data.loc[1,['HP']]

#columnlardan bazilarini secmek istersem
columnHPandAttack=data[['HP','Attack']]

#SLICING DATA FRAMES(Aralik Secme)
# Difference between selecting columns: series and dataframes
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames

# Slicing and indexing series
data.loc[1:10,"HP":"Defense"]   # 10 and "Defense" are inclusive

# Reverse slicing 
data.loc[10:1:-1,"HP":"Defense"] # REVERSE icin -1 koyduk.

# From something to end
data.loc[1:10,"Speed":] 

#FILTERING DATA FRAMES
# Creating boolean series
boolean = data.HP > 200
hıghHP=data[boolean]

#Combining Filters
firstFilter=data.HP>150
secondFilter=data.Speed>35
combinedFilteredData=data[firstFilter & secondFilter]

#Speed'e gore filtrele ama bana HP'leri goster
conditionalData=data.HP[data.Speed<15]

#TRANSFORMING DATA

#plain python functions
def div(n):
    return n/2
halfHP=data.HP.apply(div)

#or we can use lambda function
halfHPLambda=data.HP.apply(lambda n:n/2)

#YENI BIR COLUMN YARATMA
# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()

#INDEX OBJECTS AND LABELED DATA
#   index:sequence of label

#our index name is
print(data.index.name) # it gives #
#lets change it
data.index.name='indexName'
headData2=data.head()

#index uzerinde islem yaparken asil data bozulmasin diye bunu kopyalayalim.
data2=data.copy()
#indexleri 100den 900'e kadar ayarlayalim. Gereksiz ama nasil yapildigini ögren.
data2.index=range(100,900,1)
#data.index=data['#'] yaparsak indexi 1'den itibaren yeni bir feature olarak olusturuyordu.


#%%
#HIERARCHICAL INDEXING
#ONEMLI !!!
#Verideki herhangi bir feature'i index olarak atayip datayi daha rahat okuyabilirim.

data2=data.set_index(['Type 1','Type 2']) # Type 1: OuterIndex, Type 2:InnerIndex


#%% PIVOTING DATA FRAMES
# pivoting: reshape tool
# featurelar value olarak gelip, valulari feature olarak atayabiliriz. Tabloda yer degistirme yapar pivot.
dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)

# pivoting
df.pivot(index="treatment",columns = "gender",values="response")

#%% STACKING and UNSTACKING DATAFRAME
# birden fazla index icin herhangi bir boyuna indexi baslik olarak enine hale getirebilir ve bu indexten kurtulabiliriz.
# deal with multi label indexes
# level: position of unstacked index
# swaplevel: change inner and outer level index position

df1 = df.set_index(["treatment","gender"])
df1
# lets unstack it
# level determines indexes
unstackTreatment=df1.unstack(level=0) #index0'da treatment var. bu indexi enine yazarak index olmaktan kurtarir.

#INNER VE OUTER INDEXLERIN YERINI DEGISTIRME
df2=df1.swaplevel(0,1)

#%% MELTING
#Pivoting'in tersidir.

# df.pivot(index="treatment",columns = "gender",values="response")
pd.melt(df,id_vars="treatment",value_vars=["age","response"]) 
# MELT: INDEX,VARIABLE,VALUE donduruyordu
#   burada index treatment oldu. variable age oldu. value da response oldu.


#%% CATEGORICALS AND GROUPBY

# according to treatment take means of other features
df.groupby("treatment").mean()   # mean is aggregation / reduction method
# there are other methods like sum, std,max or min

# we can only choose one of the feature
df.groupby("treatment").age.max() 

# Or we can choose multiple features
df.groupby("treatment")[["age","response"]].min() 


