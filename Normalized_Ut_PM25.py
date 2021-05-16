import numpy as np
import pandas as pd

Month=12

def Normalized( rows, cols, Normal):
    Total=Normal.sum(axis=1)
    for i in range(0, rows):
        for j in range(0, cols):
            Normal[i,j]=Normal[i,j]/Total[i]
    return Normal

def Mass(Normal,rows,cols,list):
    Normal=Normalized(rows,cols,Normal)
    Mass_Column=[]
    cm=pow(10,7)
    convert_to_ug_per_m3=pow(10,12)
    for i in range(0,rows):
        Mass=0
        for j in range(0,cols):
            Mass+=Normal[i][j]*(4/3)*np.pi*(list[j]/(2*cm))**3*1.5
        Mass_Column.append(Mass*convert_to_ug_per_m3)
    return Mass_Column

def Excel(df_list,file,sheet,itr):
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    for i in range(0,itr):
        # Write each dataframe to a different worksheet.
        df_list[i].to_excel(writer, sheet_name=sheet[i])
    writer.save()


FileName=(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\RawData.xlsx")
xls=pd.ExcelFile(FileName)
temp=pd.read_excel(xls, 0)
rows,cols=temp.shape
cols=cols-1
list=temp.columns.values.tolist()
list.pop(0)
df_Mass=[]
for i in range(0,Month):
    Normal=(pd.read_excel(xls,i)).to_numpy()
    Normal = np.delete(Normal, 0, 1)
    Mass_Column=Mass(Normal,rows,cols,list)
    df_Mass.append(pd.DataFrame(Mass_Column,columns=['Normalized mass (In ug/m3)']))


Normalized_Mass=(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Normalized_Mass.xlsx")
sheet=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Excel(df_Mass,Normalized_Mass,sheet,Month)
