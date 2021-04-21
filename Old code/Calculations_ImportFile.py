# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:15:27 2021

@author: Somendra Singh Jadon
"""

#Write down the Chemical properties and compostition

# Black Carbon, Organic Carbon, SNA, Chlorides

import xlrd
import xlsxwriter
import numpy as np
import miepython as mp

N_re=1                                                                        # Real part of RI of medium(water in this case)                         
N_im=0                                                                        # Imaginary part of RI of water
N=complex(float(N_re),float(N_im))
n_comp=4                                                                      # Number of components in air
M_re=[1.57, 1.5, 1.38,1.6]                                                    # Real part of particle R.I
M_im=[0.53,0,0,0]   
cm=10000000                                                          # Imaginary part of particle R.I                           
wavl=550/cm


#dia=[size/cm, size/cm, size/cm, size/cm]                                       # Diameter in cm                            

frac=[0.05,0.55,0.1,0.3]


def Output_initialize(sheetRead, sheetWrite):
    for i in range(2,130):
        sheetWrite.write(0,i, (sheetRead.cell_value(0,i)))

def Excel(loc):
    wb = xlrd.open_workbook(loc) 
    return wb.sheet_by_index(0)

def Area(dia):
    return (np.pi*(dia/(2))**2)

def anisotropy(sheetWriteG,g,col,index):
    sheetWriteG.write(2+index,col,g)
    

def Extinction_coeff(sheetWriteG,dia,col):
    global M_re, M_im, N_re, wavl
    Qext=[]
    X=(3.14*dia*N_re)/wavl
    for i in range(0,n_comp):
        Z=complex(float(M_re[i]),float(-M_im[i]))
        ans=mp.mie(Z,X)
        Qext.append(ans[0])
        anisotropy(sheetWriteG,ans[3],col,i)
    return Qext

def Update_excel(sheetWriteUt ,Ut_individual,time,col):
    global n_comp
    for i in range(0,n_comp):
        sheetWriteUt.write(time*5+i+2,col,Ut_individual[i])
        k=i+1
    sheetWriteUt.write(time*5+k+2,col,sum(Ut_individual))
    
def Update_Ut(sheetRead,sheetWriteUt,Qext,A,col,time):
    global n_comp, frac
    NumConcentration=sheetRead.cell_value(time,col)
    Ut_individual=[]
    for i in range(0,n_comp):
        Ut_individual.append(NumConcentration*A*frac[i])
    Update_excel(sheetWriteUt,Ut_individual,time,col)
    
    
    
def Mother_function(sheetRead,sheetWriteUt,sheetWriteG,col,time):
    global cm
    dia=sheetRead.cell_value(0,col)/cm
    print('dia= ', dia)
    A=Area(dia)
    Qext=Extinction_coeff(sheetWriteG,dia,col)
    Update_Ut(sheetRead,sheetWriteUt,Qext,A,col,time)



Excel_fileName="RawData1.xlsx"
sheetRead=Excel(Excel_fileName)
xlsx_Ut = xlsxwriter.Workbook('Ut_Values.xlsx')
sheetWriteUt=xlsx_Ut.add_worksheet()
xlsx_g = xlsxwriter.Workbook('g_Values.xlsx')
sheetWriteG=xlsx_g.add_worksheet()
Output_initialize(sheetRead, sheetWriteG)
Output_initialize(sheetRead, sheetWriteUt)

for i in range(2,130):
    print('i= ', i)
    for j in range(0,11):
        Mother_function(sheetRead,sheetWriteUt,sheetWriteG,i,j)
        
    
xlsx_Ut.close()
xlsx_g.close()




