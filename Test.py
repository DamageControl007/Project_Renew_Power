import pandas as pd
import numpy as np
import miepython as np


A=[]

for i in range(0,2):
    A.append([])
    for j in range(0,5):
        A[i].append(j)
# print(A)
#
# print(A[1][4])

FileName="RawData1.xlsx"
RawData=pd.read_excel(FileName)
print(RawData.columns)
list=RawData.columns
print("list=", list)
list2=RawData.columns.values.tolist()
list2.pop(0)
list2.pop(0)
print("new list=", list2)
print("number of elemnts in list", len(list2))
# data_top = data.head()
# print(data_top)
# # iterating the columns
#
# for row in data_top.index:
#     print(row, end = " ")
