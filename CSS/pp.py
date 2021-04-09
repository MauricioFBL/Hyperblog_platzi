import pandas as pd
import numpy as np
# print(pd.NA | False)
# print([10,8,5,0] + [0,1,6,12])
# df = pd.DataFrame([1,2,3])
# print(df.shape)
# print(pd.Series([10,8,5,0]) - pd.Series([0,1,6,12]))
df = pd.DataFrame({
    'edad' :     [ 10, 9, 13, 14, 12, 11, 12],
    'cm' : [ 115, 110, 130, 155, 125, 120, 125],
    'pais' :    [ 'co', 'mx', 'co', 'mx', 'mx', 'ch', 'ch'],
    'genero' :  [ 'F', 'M', 'M', 'M', 'F', 'F', 'F'],
    'Q1' : [ 5, 10, 8, np.nan, 7, 8, 3],
    'Q2' : [ 7, 9, 9, 8, 8, 8, 9.]
}, index = ['Ana','Benito','Camilo','Daniel','Erika','Paola','Gabriela']) 

df2=pd.DataFrame({
    'edad' :     [ 10, 9, 13, 14, 12, 11, 12],
    'cm' : [ 115, 110, 130, 155, 125, 120, 125],
    'pais' :    [ 'co', 'mx', 'co', 'mx', 'mx', 'ch', 'ch'],
    'genero' :  [ 'F', 'M', 'M', 'M', 'F', 'F', 'F'],
    'Q1' : [ 5, 10, 8, np.nan, 7, 8, 3],
    'Q2' : [ 7, 9, 9, 8, 8, 8, 9.]
}, index = ['Ana2','Benito2','Camilo2','Daniel','Erika','Paola','Gabriela']) 
# idx = pd.IndexSlice
# dfmi.loc[idx[:, 'B0':'B1'], :]
# print(df.groupby(['genero'])['cm'].agg([np.mean,np.std]))
# print(df.groupby(['genero'])['edad'].agg([np.mean,np.std]))
# print(df['edad'] >= 12)
# print(df.iloc[[4],[2]])
# print(df[(df['edad'] > 12) & (df['pais']=='mx')])
# print(np.array([10,8,5,0]) * np.array([0,1,6,12]))
# print(df.loc[['Ana'],['cm']])
# print(df.describe(include='all'))
# print(df.dtypes)
# df.convert_dtypes
# print(df.dtypes)
print(df+df2)

# print(df.query("(edad >= 12) & (cm < 130) & (Q1 > 5)")['Q2'])