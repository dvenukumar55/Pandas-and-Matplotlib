import pandas as pd
'''
df=pd.read_csv(r"C:\Users\ADMIN\OneDrive\Desktop\my_py\Pandas\data.csv")

#removes irrelevant data
df=df.drop(columns=["legendary"])


#handle missing data
df=df.dropna(subset=["type2"])
df=df.fillna({"type2":"no value"})


#fix inconsistent values
df["type1"]=df["type1"].replace({"Grass":"GRASS",
                                 "Water":"WATER"})


#standardise text
df["name"]=df["name"].str.upper()


#fix datatypes
df["legendary"]=df["legendary"].astype(bool)


#remove duplicates
df=df.drop_duplicates()


print(df.to_string())
'''