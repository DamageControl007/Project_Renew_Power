# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:57:56 2021

@author: Asus
"""

import xlrd
import xlsxwriter as xlsxwriter
import numpy as np

def getExcel(loc):
    wb=xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)
    return sheet

def CreateExcel(name):
    NewFile = xlsxwriter.Workbook(name)
    return NewFile

def TotalSum(InputSheet, time):
    Whole=0
    for i in range(0,InputSheet.ncols-2):
        Whole+=InputSheet.cell_value(time+1,i+2)
    
    return Whole

def initalize(InputSheet, OutputSheet,Time,Morning):
    for i in range(0,InputSheet.ncols-2):
        OutputSheet.write(0,i+1,InputSheet.cell_value(0,i+2))
    for i in range(0,Time):
        OutputSheet.write(i+1,0, str(i+Morning)+":00")
    
def Update_Cumulative(time,InputSheet, OutputSheet):
    add=0
    Total=TotalSum(InputSheet,time)
    for i in range(0,InputSheet.ncols-2):
        add+=InputSheet.cell_value(time+1,i+2)/Total
        OutputSheet.write(time+1,i+1,add)


FileName="CumulativeValues.xlsx"
loc="RawData1.xlsx"
DataSheet=getExcel(loc)
xlsx_graph=CreateExcel(FileName)
CumulativeSheet=xlsx_graph.add_worksheet()
xlsxwriter.Workbook
Time=10
Morning=8
initalize(DataSheet,CumulativeSheet,Time,Morning)

for i in range (0,Time):
    Update_Cumulative(i,DataSheet,CumulativeSheet)

xlsx_graph.close()
    

