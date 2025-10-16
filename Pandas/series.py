import pandas as pd

# print(pd.__version__)

#series=it is 
# pandas 1D labeled Array that can hold any datatype

d1=[234,23,34,45,56]
s1=pd.Series(d1,index=['a','b','c','d','e'])
print(s1)
s1.loc['c']=3456
print(s1)
print(s1.loc['e'])
print(s1.iloc[4])  #loc,iloc
print(s1[s1>45])

d2=['a','b','c','b']
s2=pd.Series(d2)
print(s2)

d3=[True,False]
s3=pd.Series(d3)
print(s3)

d4=[None]
s4=pd.Series(d4)
print(s4)

marks={
    'm1':45,
    'm3':46,
    'm4':39
}
s5=pd.Series(marks)
print(s5)

s5.loc['m4']+=21
print(s5)