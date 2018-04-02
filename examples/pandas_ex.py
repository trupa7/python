import numpy as np
import  pandas as pd
from datetime import  datetime
x=[]
#load csv file
# for line in open('data2.csv'):
#     row=line.split(',')
#
#     sample=map(float,row)
#     x.append(row)
#
# print(x)
# x=np.array(x)
# print(x.shape)

A=pd.read_csv('dataset.csv',header=None)
# print('type',type(A))
# print('info',A.info())
#head
# print(A.head(10))
#convert to matrix
M=A.as_matrix()
# print(M)
# print(A[0][0])
# print(A.ix[0])
# print(A[[0,2]])#get column and row
# print(A[A[0]<20]) #column 1 < 20
# print(A[0]<20) #boolen condition


# df=pd.read_csv('international-airline-passengers.csv',engine='python')
# df.columns=["month","Passengers"]
# print(df.columns) #columns
# print(df["Passengers"]) #print perticular column
# df['ones']=1 #add new column with value 1
# df['dt']=df.apply(lambda row : datetime.strptime(row['month'],"%Y-%m"),axis=1) #month to time
#
# print(df.head())

#join csv
t1=pd.read_csv("table1.csv")
t2=pd.read_csv("table2.csv")
m=pd.merge(t1,t2,on='user_id')
print(m)