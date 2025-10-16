import pandas as pd

#dataframe=a tabular datastructure with rows and columns(2D)

data={
    'names':['venu','sudheer','shankar','abhi'],
    'marks':[48,34,40,39]
}
df=pd.DataFrame(data,index=[1,2,3,4])
print(df)
print(df.loc[1])
print(df.iloc[0])

#adding new column
df['clg']=['avih','cbit','vbit','mvsr']
print(df)

#adding new row
newrow=pd.DataFrame([{'names':'vamshi','marks':33,'clg':'kmit'},
                     {'names':'vamini','marks':13,'clg':'asra'}]
                    ,index=[5,6])
df=pd.concat([df,newrow])
print(df)
'''

# csv=comma separated values
# json=javascript object notation
#IMPORTING
'''
df = pd.read_csv(r'C:\Users\ADMIN\OneDrive\Desktop\my_py\Pandas\data.csv')
print(df)
'''

#SELECTION
'''
df = pd.read_csv(r'C:\Users\ADMIN\OneDrive\Desktop\my_py\Pandas\data.csv',index_col="name")\

# selection by columns

print(df["name"].to_string())
print(df["height"].to_string())
print(df["weight"].to_string())
print(df["no","name"].to_string())


# selection by rows

print(df.loc[0])

print(df.loc["Pikachu",["no","name"]])


res=input("enter name: ")
try:
    print(df.loc[res])
except KeyError:
    print(f"{res} not found")    
