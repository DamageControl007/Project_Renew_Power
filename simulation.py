import numpy as np
import matplotlib.pyplot as plt
import miepython as mp
import pandas as pd
import random
import datetime
from pysolar.solar import *


def Anisotropy(Particle_index ,dia_index):
    return df_g.iat[Particle_index,dia_index]

def diameter(Time):
    global cols
    e=random.uniform(0,1)
    list=df_cum.columns.values.tolist()

    list.pop(0)
    for i in range(0,cols):
        if e<=df_cum.iat[Time,i+1]:
            return list[i], i


def Initialize_Dirctions(Time):
    global morning
    global day,Month
    tame=Time+morning-6
    Month=month+1
    if tame<0:
        tame=24+tame
    date=datetime.datetime(2020,Month,day,tame,30,00,00,tzinfo=datetime.timezone.utc)
    a=(get_altitude(28.7041, 77.1025, date))
    b=(get_azimuth(28.7041, 77.1025, date))
    theta1=np.pi/2-np.deg2rad(a)
    theta2=np.deg2rad(b)
    theta3=np.pi/2 - theta2
    Vx=np.sin(theta1)*np.cos(theta2)
    Vy=np.sin(theta1)*np.cos(theta3)
    Vz=np.cos(theta1)
    norm=np.sqrt(Vx**2 + Vy**2 + Vz**2)
    return Vx/norm,Vy/norm,Vz/norm


def Simulate(itr,Time,mass_factor):
    global direct
    dia,dia_index=diameter(Time)
    Ut=Interaction_coeff(Time)*mass_factor
    print("Ut= ", Ut)
    Vx,Vy,Vz=Initialize_Dirctions(Time)

    for i in range(0,itr):
        if (i%(itr/10)==0):
            print("UtxL= ", Ut*pow(10,5)/Vz)
            print(i*100/itr,"%")
        #Ux,Uy,Uz=initialize(Time)
        Ux,Uy,Uz=Vx,Vy,Vz
        x,y,z=[0,0,0]
        e=random.uniform(0,1)
        s=np.log(e)/Ut*(-1)
        x,y,z=Update_Path(x,y,z,s,Ux,Uy,Uz)
        if z>100000:
            direct+=1
        while Boundary_check(x,y,z):
            s=np.log(e)/Ut*(-1)
            dia,dia_index=diameter(Time)
            Particle_type=Particle_Index(Time,dia_index)
            g=Anisotropy(Particle_type,dia_index)
            Ux,Uy,Uz=Direction_cosines(Ux,Uy,Uz,g)
            x,y,z=Update_Path(x,y,z,s,Ux,Uy,Uz)



def Interaction_coeff(Time):
    arr=df_Ut.to_numpy()
    print(arr[Time*5+4].sum())
    print((Time*5+4))
    return (arr[Time*5+4].sum()-(Time*5+4))


def Particle_Index(Time,dia_index):
    global n_comp
    prob=[]
    for i in range(0,n_comp):
        prob.append(df_Ut.iat[Time*5+i,dia_index]/df_Ut.iat[Time*5+n_comp,dia_index])
    e=random.uniform(0,1)
    limit=0
    for i in range(0,n_comp):
        limit+=prob[i]
        if e<=limit:
            return i
    return (n_comp-1)


def Update_Path(x,y,z,s,Ux,Uy,Uz):
    x=x+s*Ux
    y=y+s*Uy
    z=z+s*Uz
    return x,y,z

def Boundary_check(x,y,z):
    global path, mass
    Lx=pow(10,10)
    Ly=pow(10,10)
    Lz=100000
    if z>Lz:
        mass+=1
        return False
    elif z<0:
        return False
    else:
        return True

def Direction_cosines(Ux,Uy,Uz,g):
    Cosines=[Uz,Ux,Uy]
    e=random.uniform(0,1)
    phi=e*2*3.14
    e=random.uniform(0,1)
    if abs(g)<0.001:
        g=1
    cos=(1/(2*g))*(1 + g*g - ((1-g*g)/(1+g*(2*e - 1)))**2)
    if abs(cos)>1:
        return Cosines
    theta=np.arccos(cos)
    sin_theta=np.sin(theta)
    cos_theta=np.cos(theta)
    sin_phi=np.sin(phi)
    cos_phi=np.cos(phi)
    if abs(Cosines[0])>0.99999:
        Cosines[0]=np.sign(Cosines[0])*cos_theta
        Cosines[1]=sin_theta*cos_phi
        Cosines[2]=sin_theta*sin_phi
    else:
        Uz,Ux,Uy=Cosines
        Usqr=np.sqrt(1-Uz**2)
        Cosines[0]=-sin_theta*cos_phi*Usqr + Uz*cos_theta
        Cosines[1]=(sin_theta*(Uz*Ux*cos_phi - Uy*sin_phi)/(Usqr)) + Ux*cos_theta
        Cosines[2]=(sin_theta*(Uz*Uy*cos_phi + Ux*sin_phi)/(Usqr)) + Uy*cos_theta
    return Cosines

# Global Variables


n_comp=4

itr=pow(10,5)

morning=8
Time_Range=10
photon=[]
print("Enter month: ")
Month=int(input())
print("enter date: ")
day=int(input())
print("Enter time in 24 hour format (only mention the hour mark)")
Day_Time=int(input())
print("Enter PM2.5 concentration in ug/m3: ")
PM25=int(input())
#initialize for index purpose
month=Month-1
Ut_file=pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Ut_values.xlsx")
Cumulative_file=pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Cumulative_values.xlsx")
Anisotropy_file = pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\All_anisotropy_values.xlsx")
Normalized_mass_file=pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Normalized_Mass.xlsx")

df_Ut=pd.read_excel(Ut_file, month)
df_cum=pd.read_excel(Cumulative_file, month)
df_g= pd.read_excel(Anisotropy_file, month)
df_mass=pd.read_excel(Normalized_mass_file,month)

rows,cols=df_Ut.shape
cols=cols-1
nm=1
Time=Day_Time-morning
mass_factor=(PM25*0.3)/df_mass.iat[Time,1]
print("mass factor= ", mass_factor)
for i in range(0,nm):
    path=0
    mass=0
    Month=1
    direct=0
    Simulate(itr,Time,mass_factor)
    print("direct=", direct/itr)
    photon.append(direct/itr)
    print(mass/itr)

# x_axis=[]
# for i in range(0,Time_Range):
#     x_axis.append(i+morning)
#
# plt.plot(x_axis,photon)
# plt.show()
