# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 04:41:11 2021

@author: VolkanKarakuş
"""

#%%
#global: defined main body in script
#local: defined in a function
#built in scope: names in predefined built in scope module such as print,len

x=2
def f():
    x=3
    return x
print(x)    #x=2 global scope
print(f())  #x=3 local scope


#%% NESTED FUNCTION (ic ice)

def square():
    'return square of value'
    def add():
        'add two local variables'
        x=2
        y=3
        z=x+y
        
        return z
    return add()**2
print(square())

####default arguments###
def f(a,b=1,c=2):
    y=a+b+c
    
    return y
print(f(5))
#what if we want to change default arguments
print(f(5,4,3))

###flexible arguments  *ARGS ###
def fx(*args):
    for i in args:
        print(i)

print(fx(1))
print(fx(1,2,3,4))

###flexible arguments *KWARGS ###
def a(**kwargs):
    'print key and value of dictionary'  # KWARGS USES IN DICTIONARY
    for key,value in kwargs.items():
        print(key,' ',value)
        
a(country='spain',capital='madrid',population=12345)

#%% LAMBDA FUNCTION
# faster way of writing functions
square=lambda x:x**2
print(square(4))

tot=lambda x,y,z:x+y+z
print(tot(1,2,3))

#%% ANANYMOUS FUNCTION
#like lambda function but it can take more than one argument.
# map(func,seq): applies a function to all the items in the list.
numberList=[1,2,3,4]
y=map(lambda x:x**2, numberList)
print(list(y))

#%% ITERATORS
