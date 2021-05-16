import pandas as pd
import numpy as np
import miepython as mp
import random
import datetime
from pysolar.solar import *
import matplotlib.pyplot as plt

# def last():
#     a=[1,2,3]
#     x,y,z=a
#     print(x,y,z)
#     return 35,x
# # df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
# # list=[1,2,3]
# # d=np.zeros((2,2))
# # x,y,z=last()
# # print("x,y,z=", x,y,z)
# #
# # print(d);print("it works")
# a,b=last()
# print(a,b)
#
# Ut_file=pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Ut_Values.xlsx")
# Cumulative_file=pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Normalized_Values.xlsx")
# Anisotropy_file = pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Anisotropy_Values.xlsx")
# cols=129
# i=0
# df_Ut=pd.read_excel(Ut_file, i)
# df_cum=pd.read_excel(Cumulative_file, i)
# df_g= pd.read_excel(Anisotropy_file, i)
# def diameter(Time):
#     global cols
#     e=random.uniform(0,1)
#     list=df_cum.columns.values.tolist()
#     list.pop(0);list.pop(0);list.pop(0)
#     for i in range(0,cols):
#         if e<=df_cum.iat[Time+1,i+1]:
#             print("list=", list[i])
#             print("i=", i)
#             return list[i], i
#     return 100,i
# a,b=diameter(0)
# df_g= pd.read_excel(Anisotropy_file, 0)
# print("df_g check", df_g.iat[0,b])
# Time=0
# print("df_Ut := ", df_Ut.iat[Time*5+4,1])
# numpy_array=df_Ut.to_numpy()
#
# print("numpy array= ", numpy_array)
# print("numpy[0,1]= ", (numpy_array[Time*5+4].sum()-(Time*5+4)))
# prob=[]
# n_comp=4
# dia_index=1
# for i in range(0,n_comp):
#     print("df= ", df_Ut.iat[Time*5+i,dia_index])
#     prob.append(df_Ut.iat[Time*5+i,dia_index]/df_Ut.iat[Time*5+n_comp,dia_index])
# print("Prob= ", sum(prob))
# print((diameter(0)))
# print("HEllo", a)
# Time=0
# morning=8
# day,month=10,4
# tame=Time+morning-6
# if tame<0:
#     tame=24+tame
# date=datetime.datetime(2020,month,day,tame,30,00,00,tzinfo=datetime.timezone.utc)
# a=(get_altitude(28.7041, 77.1025, date))
# b=(get_azimuth(28.7041, 77.1025, date))
# theta1=np.pi/2-np.deg2rad(a)
# theta2=np.deg2rad(b)
# theta3=np.pi/2 - theta2
# Vx=np.sin(theta1)*np.cos(theta2)
# Vy=np.sin(theta1)*np.cos(theta3)
# Vz=np.cos(theta1)
# norm=np.sqrt(Vx**2 + Vy**2 + Vz**2)
# Ux,Uy,Uz=Vx/norm,Vy/norm,Vz/norm
# print(Ux**2+Uy**2+Uz**2)

time=[8,9,10,11,12,13,14,15,16,17]
BeerLamberts=[0.0045538
,0.068910373
,0.224095718
,0.460120545
,0.468658556
,0.536349359
,0.522843227
,0.380165418
,0.280323374
,0.057353561

]
Direct=[0.00466
,0.06897
,0.22403
,0.46147
,0.4601
,0.53689
,0.53475
,0.38196
,0.28104
,0.05764

]

plt.plot(time,Direct, marker='H', color='r', label='Direct irradiance')
plt.plot(time,BeerLamberts, marker='+', color='g', label='Beer-Lamberts value')
plt.legend(loc='lower left', bbox_to_anchor=(0.6,0.5))
plt.xlabel('Time')
plt.ylabel('I/Io')
plt.title('Simulation vs beer lambert formula (for January)')
plt.legend()
plt.show()


# FileName="RawData1.xlsx"
# RawData=pd.read_excel(FileName)
# print(RawData.columns)
# list=RawData.columns
# print("list=", list)
# list2=RawData.columns.values.tolist()
# list2.pop(0)
# list2.pop(0)
# print("new list=", list2)
# print("number of elemnts in list", len(list2))
# data_top = data.head()
# print(data_top)
# # iterating the columns
#
# for row in data_top.index:
#     print(row, end = " ")
