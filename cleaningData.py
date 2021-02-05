# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:56:23 2021

@author: VolkanKarakuş
"""

#%% 
#lets return pokemon csv and make one more list comprehension example.
#lets classify pokemons whether they have high or low speed. Our threshold is average speed.
import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv('pokemon.csv')
threshold=sum(data.Speed)/len(data.Speed)
print('Threshold :',threshold)
data['SpeedLevel']=['high' if i > threshold else 'low ' for i in data.Speed]
headDataExample=data.loc[:10,['SpeedLevel','Speed']]

headData=data.head(7) #default 5 data
columns=data.columns
shape=data.shape # 800 pokemons, 12 features
info=data.info() 

#%% EXPLOTARY DATA ANALYSIS (EDA)
#value_counts():Frequency counts
#Lets look frequency of pokemon types 

print(data['Type 1'].value_counts(dropna=False))

#QUARTILE
#Median is not a mean.
#The median is the number that is in middle of the sequence. In this case it would be 11.
#The LOWER QUARTILE(Q1)(25% QUANTILE) is the median in between the smallest number and the median i.e. in between 1 and 11, which is 6.
#The UPPER QUARTILE(Q3)(75% QUARTILE), you find the median between the median and the largest number
#    i.e. between 11 and 17, which will be 14 according to the question above.

#OUTLIERS: AYKIRI,AYRIK
#   the value that is considerably higher or lower from rest of the data.

#Q3-Q1=IQR
#Q1-1.5IQR degeri OUTLIER ALT SINIRIDIR.
#Q3+1.5IQR degeri OUTLIER UST SINIRIDIR.
#Outlier'lar max degerin uzerinde, min degerin altindadir.

#BOXPLOT
data.boxplot(column='Attack',by='Legendary') #Attack'in Legendary olup olmamasina gore boxplot.
plt.show()

#%% TIDY DATA
headData=data.head(7) #default 5 data
# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt

#MELT, ELIMIZDEKI DATA FRAME'IN KEYSINI YENI BIR COLUMN ALTINDA VALUE OLARAK YAZAR.
#   DEGERINI DE YENI BIR VALUE KEYSINE YAZAR.
#default olarak variable,value keysleri olusturur.

melted = pd.melt(frame=headData,id_vars = 'Name', value_vars= ['Attack','Defense'])
#frame,islenecek frame.
#id_vars, yeni frame'de degismeden kalsin.
#value_vars, keylerin valuelarini, melted'de bir keys olarak yazar.

#REVERSE OF MELTING(PIVOTING DATA)
pivoted=melted.pivot(index='Name',columns='variable',values='value') 
#melt default olarak variable ve value isimli columslar olusturmustu, bunu geri aldik.


#%% CONCATENATING DATA
#   we can concatenate two dataframe.
data1=data.head() #first 5 sample
data2=data.tail() #last 5 sample
concDataRow=pd.concat([data1,data2,data2],axis=0,ignore_index=True) # axis=0 : add dataframes in row (ALT ALTA)
 
data3=data['Attack'].head()
data4=data['Defense'].head()
concDataCol=pd.concat([data3,data4],axis=1,ignore_index=True) #axis=1 : add dataframes in columns (YAN YANA)

#%% CATEGORICAL DATA TYPE
# int,str,boolean gibi data type'lar ogrenmistik.
# bunlara ek olarak bir de CATEGORICAL var.
# bunun avantaji :
#   make dataframe smaller in memory
#   can be utilized for anlaysis especially for sklearn(we will learn later)

types=data.dtypes
#lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')
newtypes=data.dtypes

#%% MISSING DATA and TESTING WITH ASSERT
#missing data, daha once degeri tanimlanmamis degersiz seylerdir.
first10Value=data.head(10)
#first10Value'ya baktigimizda Charmender'in Type2'si NaN

# If we encounter with missing data, what we can do:

# leave as is
# drop them with dropna()
# fill missing value with fillna()
# fill missing values with test statistics like mean
# Assert statement: check that you can turn on or turn off when you are done with your testing of the program

# Lets chech Type 2
NaNValueofType2=data["Type 2"].value_counts(dropna =False) #dropna=False demek NaN valuelari da goster demek.
# As you can see, there are 386 NAN value

#%% 
copyData=data.copy() # copy yapmayip esitleseydim yapicagim islemler sonrasi data dosyasi da degisicekti.
#copyData=copyData['Type 2'].dropna(inplace=True) #NAN OLANLARİ DROP ETMEK.

#bu satiri copyData'ya esitlememe gerek yok,zaten inplace=True yaptik.
#yaptigimiz bu islemin dogru olup olmadigini ASSERT ile kontrol ederiz.
#assert  copyData['Type 2'].notnull().all()# bunu run ettigimizde hicbirsey dondurmedi. Yani yaptigimiz islem dogru.
# ustteki satir kaggle'da calisiyor ama spyderda hata verdi.
#%%
copyData['Type 2'].fillna('empty',inplace = True) # NaN'lari empty ile dolduralim.
assert  copyData['Type 2'].notnull().all() # returns nothing because we do not have nan values

# # With assert statement we can check a lot of thing. For example
# assert data.columns[1] == 'Name'
# assert data.Speed.dtypes == np.int


