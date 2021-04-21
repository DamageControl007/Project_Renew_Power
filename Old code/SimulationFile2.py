# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:32:04 2021

@author: Asus
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:58:11 2021

@author: Somendra Singh Jadon
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import miepython as mp
import csv
import xlrd
import xlsxwriter
import sys
from datetime import date
from pysolar.solar import *
import datetime
from solarpy import irradiance_on_plane

nm=8                                                                          #Number of hours in a day
itr=100000                                                                     #number of iterations
n_comp=4
          
    
loc1="g_Values.xlsx"
loc2="Ut_Values.xlsx"
loc3="CumulativeValues.xlsx"
def getExcel(loc):
    wb=xlrd.open_workbook(loc)
    return wb.sheet_by_index(0)

sheet1=getExcel(loc1)
sheet2=getExcel(loc2)
sheet3=getExcel(loc3)

ncols1=sheet1.ncols
ncols2=sheet2.ncols
ncols3=sheet3.ncols
print("Ncols2=", ncols2)
    

weight=[]
path=0
thru=0
front=0
mass=0
hit=0
day=15
month=4
back=0
for k in range(0,1):
    #wavl=int(sheet3.cell_value(22+k,0))                                       # Wavelenght of light in cm
    wavl=550
    wavelength=str(wavl)
    for j in range(0,nm):
        front=0
        time=j
        Time=time+8
        '''height=layer(month)
        print('height= ', height)
        boun.append(height)'''
        height=1000
        #planet.append(layer(j+5, proxy))
        x_dir=0                                                                # Initializing x coordinate
        y_dir=0                                                                # Initializing y coordinate
        z_dir=0                                                                # Initializing z coordinate
        Lz=height*100                                                          # Length of system in cm
        Ly=1000000000000000
        Lx=1000000000000000
        tame=Time-6
        if tame<0:
            tame=24+tame
        day3=15
        month=4
        date=datetime.datetime(2020,month,day,tame,30,00,00,tzinfo=datetime.timezone.utc)
        a=(get_altitude(28.7041, 77.1025, date))
        b=(get_azimuth(28.7041, 77.1025, date))
        theta1=np.pi/2-np.deg2rad(a)
        theta2=np.deg2rad(b)
        theta3=np.pi/2 - theta2
        Vx=np.sin(theta1)*np.cos(theta2)
        Vy=np.sin(theta1)*np.cos(theta3)
        Vz=np.cos(theta1)
        norm=np.sqrt(Vx**2 + Vy**2 + Vz**2)
        
        Ut=sheet2.cell_value((time+1)*5+1,ncols2-1)
        print('Ut=', Ut)
        for elf in range(0,itr):
    
            if elf%10000==0:
                print(elf*100/itr)
    
            Ux=Vx/norm
            Uy=Vy/norm
            Uz=Vz/norm
            w=1
            e=random.uniform(0,1)
            x=0
            y=0
            z=0
            e=random.uniform(0,1)
            s=-np.log(e)/Ut
            x=s*Ux
            y=s*Uy
            z=s*Uz
            system=True
            lim=0
            
            if z>Lz:
                path+=Lz
                thru+=1
                front+=1
                mass+=w
            elif z<0:
                pass
            else:
                hit+=1
                
    
                hit+=1
                path+=z
                
                
            
            while 0<=z<=Lz and system and w>0.0005:
                e=random.uniform(0,1)
                # determining the size of the particle
                for i in range(0,ncols3-1):
                    if e<sheet3.cell_value(time+1,i+1):
                        dia= sheet3.cell_value(0,i+1)
                        break
                # dermining the particle Type
                prob=[]
                for i in range(0,ncols2-2):
                    if dia<=sheet2.cell_value(0,i+2):
                        for j in range(0,n_comp):
                            denominator=sheet2.cell_value(time*5+2+n_comp,i+2)
                            if (denominator>0.0001):
                                prob.append(sheet2.cell_value(time*5+j+2,i+2)/sheet2.cell_value(time*5+2+n_comp,i+2))
                            else:
                                prob=[0.25,0.25,0.25,0.25]
                        break
                e=random.uniform(0, 1)
                lim=0
                for i in range(0, n_comp):
                    lim+=prob[i]
                    if e<=lim:
                        # Particle index
                        n=i+1
                        break
                
                for i in range(0,ncols1-1):
                    if dia<=sheet1.cell_value(0,i+2):
                        g=sheet1.cell_value(n+1,i+2)
                        break
                
                e=random.uniform(0,1)
                phi=e*2*3.14
    # =============================================================================
    #           e=random.uniform(0,1)
    #             for k in range(0,interval):
    #                 if zz[n][k]>e:
    #                     theta=(k*(180/interval)*(np.pi/180))
    #                     break
    # =============================================================================
                e=random.uniform(0,1)
                cos=(1/(2*g))*(1 + g*g - ((1-g*g)/(1+g*(2*e - 1)))**2)
                theta=np.arccos(cos)
                sin_theta=np.sin(theta)
                cos_theta=np.cos(theta)
                sin_phi=np.sin(phi)
                cos_phi=np.cos(phi)
                if abs(Uz)>0.99999:
                    Uz_1=np.sign(Uz)*cos_theta
                    Uy_1=sin_theta*cos_phi
                    Ux_1=sin_theta*sin_phi
                else:
                    Usqr=np.sqrt(1-Uz**2)
                    Uz_1=-sin_theta*cos_phi*Usqr + Uz*cos_theta
                    Ux_1=(sin_theta*(Uz*Ux*cos_phi - Uy*sin_phi)/(Usqr)) + Ux*cos_theta
                    Uy_1=(sin_theta*(Uz*Uy*cos_phi + Ux*sin_phi)/(Usqr)) + Uy*cos_theta
                Ux=Ux_1
                Uz=Uz_1
                Uy=Uy_1
                e=random.uniform(0,1)
                s=-np.log(e)/Ut
                loop=True
                decoy=True
                while loop:
                    N_re=1
                    z1=z+s*Uz
                    x1=x+s*Ux
                    y1=y+s*Uy
                    if 0<=z1<=Lz:
                        x=x1
                        y=y1
                        z=z1
                        hit+=1
                        path+=s
                        break
                    elif z1>Lz:
                        d=abs((Lz-z)/Uz)
                        z1=Lz
                        x1=x+d*Ux
                        y1=y+d*Uy
                        path+=d
                        if x1>Lx/2 or x1<-Lx/2 or y1>Ly/2 or y1<-Ly/2:
                            system=False
                            break
    
    
                        if N_re*np.sqrt(1-Uz**2)<0:
                            z=Lz
                            Uz=-Uz
                            s=s-d
                            x=x1
                            y=y1
                            
                        else:
                            front+=1
                            x=x1
                            y=y1
                            z=z1
                            #no detector case
                            loop=False
                            system=False
                            break
                            #for detector case
                            sin=(N_re/M_re)*np.sqrt(1-Uz**2)
                            Uy=Uy*(N_re/M_re)
                            Ux=Ux*(N_re/M_re)
                            norm=np.sqrt(Ux**2+Uy**2+Uz**2)
                            Ux=Ux/norm
                            Uy=Uy/norm
                            Uz=Uz/norm
                            d1=abs(0.1/Uz)
                            x=x + d1*Ux
                            y=y + d1*Uy
                            sin=M_re*sin
                            Uz=np.sqrt(1-sin**2)
                            Uy=(M_re)*Uy
                            Ux=(M_re)*Ux
                            norm=np.sqrt(Ux**2+Uy**2+Uz**2)
                            Ux=Ux/norm
                            Uy=Uy/norm
                            Uz=Uz/norm
                            d2=abs((sensor_z-z)/Uz)
                            x=x + d2*Ux
                            y=y + d2*Uy
                            radius=(x-sensor_x)**2+(y-sensor_y)**2
                            if radius<=sensor_area/3.14:
                                photon+=(1-trans)
                                print('photon= ', photon)
                            break
                            
    
                    else:
                        z=0
                        d=abs(z/Uz)
                        path+=d
                        x1=x+d*Ux
                        y1=y+d*Uy
                        if x1>Lx/2 or x1<-Lx/2 or y1>Ly/2 or y1<-Ly/2:
                            system=False
                            break
    
                        if N_re*np.sin(np.arccos(Uz))<0:
                            z=0
                            x=x1
                            y=y1
                            s=s-d
                            Uz=-Uz
                        else:
                            z=z1
                            system=False
                            break
    
                #russian roulette
                if w<0.001:
                      m=10
                      e=random.uniform(0,1)
                      if e<=1/m:
                          w=w*m
                      else:
                          w=0        
       
        weight.append(front/itr)

DAY=[8,9,10,11,12,13,14,15]
plt.plot(DAY,weight)
plt.show()
# =============================================================================
#         weight.append(mass/itr)
#         print('Front scattering: ', front*100/itr, ' %')
#         aaa[k].append(mass/itr)
#         distance.append((path/itr)/Lz)
#         solar.append(mass*power/itr)
#         knight.append(back/itr)
#         absorption.append(sum(absorb))
#         terminate.append(front*100/itr)
#         add1=0
#         add2=0
#         x_axis.append(mug) 
#         y_axis.append(yes/itr)
#         direct.append(thru/itr)
#         pm.append(pm25)
# =============================================================================

print('I/Io=', front/itr)

# =============================================================================
# aveg=sum(UtxLo)/14
# 
# locs = ["upper left", "lower left", "center right"]
# 
# print('I/Io= ', direct)
# print('UtxLo ', UtxLo)
# exp=[]
# for i in range(0,nm):
#     exp.append(np.exp(-UtxLo[i]))
# # =============================================================================
# # for i in range(0,ggmu):
# #     plt.plot(time, aaa[i],'-o',color='r', label= 'I/Io')
# # =============================================================================
# plt.plot(time,direct, '-o',label='Unscattered intensity')
# plt.plot(time,weight, '-o', label='I/Io (Total intensity)')
# plt.legend(loc='lower left', bbox_to_anchor=(0.6,0.5))
# plt.xlabel('Time ')
# plt.ylabel('I/Io')
# plt.title('Date: 15th April')
# plt.legend()
# plt.show()
# 
# plt.plot(time, direct, '-o', label='I/Io (unscattered intensity)')
# plt.plot(time, exp, '-o', marker=11, label='beer lamberts law values')
# plt.xlabel('time')
# plt.ylabel('I/Io')
# plt.title('Date: 15th April')
# plt.legend()
# plt.show
# =============================================================================

# =============================================================================
# fig, ax1=plt.subplots()
# 
# color = 'tab:blue'
# ax1.set_xlabel('time (24 hour)')
# ax1.set_ylabel('I/Io', color=color)
# ax1.plot(time, weight, '-o', color=color, label='I/Io')
# ax1.tick_params(axis='y', labelcolor=color)
# plt.legend()
# 
# ax2=ax1.twinx()
# color = 'tab:red'
# ax2.set_ylabel('Normalized path traveled', color=color)  # we already handled the x-label with ax1
# ax2.plot(time, distance, '-o', color=color, label='Photon path length')
# ax2.tick_params(axis='y', labelcolor=color)
# 
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.title('Relationship between I/Io and photon path length')
# plt.legend()
# plt.show()
# 
# 
# plt.plot(time,results, '-o', label= 'PM2.5' )
# 
# plt.xlabel('time')
# plt.ylabel('ug/m^3')
# plt.title(heading)
# plt.legend()
# plt.show()
# 
# =============================================================================
# =============================================================================
# plt.plot(time, boun, '-o', color='b', label= 'boundary layer height' )
# plt.plot(time,distance, '-o', color='r',label='distance covered')
# plt.xlabel('time')
# plt.ylabel('meter')
# plt.title(heading)
# plt.legend()
# plt.show()
# =============================================================================
# =============================================================================
# print('I/Io= ', weight)
# print('PBLH= ', boun)
# 
# fig, ax1=plt.subplots()
# 
# color = 'tab:blue'
# ax1.set_xlabel('time (24 hour)')
# ax1.set_ylabel('ug/m^3', color=color)
# ax1.plot(time, results, '-o', color=color, label='PM2.5')
# ax1.tick_params(axis='y', labelcolor=color)
# plt.legend()
# 
# ax2=ax1.twinx()
# color = 'tab:red'
# ax2.set_ylabel('Normalized path traveled', color=color)  # we already handled the x-label with ax1
# ax2.plot(time, distance, '-o', color=color, label='Photon path length')
# ax2.tick_params(axis='y', labelcolor=color)
# 
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.title('Relationship between PM2.5 and photon path length')
# plt.legend()
# plt.show()
# =============================================================================


# =============================================================================
# with open(heading + '_'+ wavelength + ' nm'+".csv", 'w', newline='') as f:
#     thewriter=csv.writer(f)
#     thewriter.writerow(['Normalised weigth L/Lo vs volume fraction'])
#     thewriter.writerow(['wavelength'])
#     thewriter.writerow([ wavelength])
#     thewriter.writerow(['Time', 'I/Io', 'backscattering','pm2.5','PBLH', 'UtxLo'])
#     for i in range(0,nm):
#         thewriter.writerow([time[i], weight[i], knight[i], pm[i], boun[i], UtxLo[i]])
# =============================================================================

        





        



