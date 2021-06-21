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

# time=[8,9,10,11,12,13,14,15,16,17]
# BeerLamberts=[0.0045538
# ,0.068910373
# ,0.224095718
# ,0.460120545
# ,0.468658556
# ,0.536349359
# ,0.522843227
# ,0.380165418
# ,0.280323374
# ,0.057353561
#
# ]
# Direct=[0.00466
# ,0.06897
# ,0.22403
# ,0.46147
# ,0.4601
# ,0.53689
# ,0.53475
# ,0.38196
# ,0.28104
# ,0.05764
#
# ]
#
# plt.plot(time,Direct, marker='H', color='r', label='Direct irradiance')
# plt.plot(time,BeerLamberts, marker='+', color='g', label='Beer-Lamberts value')
# plt.legend(loc='lower left', bbox_to_anchor=(0.6,0.5))
# plt.xlabel('Time')
# plt.ylabel('I/Io')
# plt.title('Simulation vs beer lambert formula (for January)')
# plt.legend()
# plt.show()


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





# CHecking the behaviour of Extinction_coeff

cm=pow(10,7)
initial=50
add=10
dia=initial
M_re1=1.57                                                 # Real part of particle R.I
M_im1=0.53
N_re=1
M1=complex(float(M_re1),float(-M_im1))
M_re2=1.50                                                 # Real part of particle R.I
M_im2=0
N_re2=1
M2=complex(float(M_re2),float(-M_im2))
M_re3=1.38                                                 # Real part of particle R.I
M_im3=0
N_re=1
M3=complex(float(M_re3),float(-M_im3))
M_re4=1.6                                                 # Real part of particle R.I
M_im4=0
N_re=1
M4=complex(float(M_re4),float(-M_im4))
frac=[0.05,0.55,0.1,0.3]

wavl=550/cm
extinction1=[]
extinction2=[]
extinction3=[]
extinction4=[]
diameter=[]
interaction1=[]
interaction2=[]
interaction3=[]
interaction4=[]
size=[]
pm25=200

for i in range(0,145):
    DIA=dia/cm
    N=(pm25*pow(10,-12))/(1.5*(4/3)*np.pi*(DIA/2)**3)
    A=np.pi*(DIA/2)**2
    X=(3.14*DIA*N_re)/wavl
    ans1=mp.mie(M1,X)
    Qext1=ans1[0]
    Ut1=Qext1*A*N
    ans2=mp.mie(M2,X)
    Qext2=ans2[0]
    Ut2=Qext2*A*N
    ans3=mp.mie(M3,X)
    Qext3=ans3[0]
    Ut3=Qext3*A*N
    ans4=mp.mie(M4,X)
    Qext4=ans4[0]
    Ut4=Qext4*A*N
    extinction1.append(Qext1)
    interaction1.append(Ut1)
    extinction2.append(Qext2)
    interaction2.append(Ut2)
    extinction3.append(Qext3)
    interaction3.append(Ut3)
    extinction4.append(Qext4)
    interaction4.append(Ut4)
    size.append(A)
    diameter.append(dia)
    dia+=add

total_Ut=[]

for i in range(0,145):
    total_Ut.append(interaction1[i]+interaction2[i]+interaction3[i]+interaction4[i])

#plt.plot(diameter,extinction1, color='r')
# plt.plot(diameter,extinction1, color='b', label="RI=1.57-i0.53")
# plt.plot(diameter,extinction2, color='r', label="RI=1.5")
# plt.plot(diameter,extinction4,color='purple', label="RI=1.6")
# plt.plot(diameter,extinction3, color='g', label="RI=1.38")
plt.plot(diameter,interaction1, color='b', label="RI=1.57-i0.53")
plt.plot(diameter,interaction2, color='r', label="RI=1.5")
plt.plot(diameter,interaction4,color='purple', label="RI=1.6")
plt.plot(diameter,interaction3, color='g', label="RI=1.38")

#plt.plot(diameter,size, color='green')
plt.xlabel("diameter (in nm)")
#plt.ylabel("Extinction efficiency")
#plt.ylabel("Interaction coefficient")
plt.ylabel("Extinction efficiency")

plt.title("Comparing Ut of different RI")
plt.legend()
plt.show()
val=10
Height=[0]*val
print(Height)


def Number(Mass,dia):
    V=(4/3)*np.pi*((dia/2)**3)
    N=(Mass/V)*(pow(10,-12)/1.5)
    return N
def Area(dia):
    A=np.pi*(dia/2)**2
    return A

cm=pow(10,7)
Mass=200   #in ug/m3
dia1=500/cm   #in nm
dia2=200/cm   #in nm
x=0.8
frac=[x,1-x]
M_re=1.5                                                 # Real part of particle R.I
M_im=0
N_re=1
wavl=550/cm
M=complex(float(M_re),float(-M_im))
X1=(3.14*dia1*N_re)/wavl
ans1=mp.mie(M,X1)
X2=(3.14*dia2*N_re)/wavl
ans2=mp.mie(M,X2)
Ut1=Number(Mass*frac[0], dia1)*Area(dia1)*ans1[0]
Ut2=Number(Mass*frac[1], dia2)*Area(dia2)*ans2[0]
print("Ut1= ", Ut1)
print("Ut2= ", Ut2)
print("total Ut= ", Ut1+Ut2)
