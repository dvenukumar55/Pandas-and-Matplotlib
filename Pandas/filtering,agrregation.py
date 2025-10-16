import pandas as pd

# df=pd.read_csv(r"C:\Users\ADMIN\OneDrive\Desktop\my_py\Pandas\data.csv")
# print(df)
'''
res1=df[df["height"]>=2]
print(res1)

res2=df[df["weight"]>=3]
print(res2)

res3=df[df["legendary"]== 1]
print(res3)

res4=df[(df["type1"]=="Water") |
        (df["type2"]=="Water")]
print(res4)


res5=df[(df["type1"]=="Grass")&
        (df["type2"]=="Poison")]
print(res5) 
'''

#AGGREGATE FUNCTIONS
'''
df=pd.read_csv(r"C:\Users\ADMIN\OneDrive\Desktop\my_py\Pandas\data.csv")

#whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))

#single column

print(df["height"].mean())
print(df["height"].sum())
print(df["height"].min())
print(df["height"].max())
print(df["height"].count())#give no.of non null values

      
#groupby()

group=df.groupby("type1")
print(group["height"].mean())
print(group["height"].sum())
print(group["height"].max())
print(group["height"].min())
print(group["height"].count())
'''