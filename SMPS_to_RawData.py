import numpy as np
import pandas as pd

Original_Data=pd.ExcelFile(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Original_Data.xlsx")
df_Raw=pd.read_excel(Original_Data, 0)
list=df_Raw.columns.values.tolist()
list.pop(0)
Raw_arr=df_Raw.to_numpy()
Raw_arr = np.delete(Raw_arr, 0, 1)
n_rows,n_cols=Raw_arr.shape

#Starting time
Morning=8

#Total time for simulation
Time_Range=10

#Resolution of SMPS (factor)
Factor=64

#print(n_rows,n_cols)

#For January
Jan_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,31):
            temp=Raw_arr[i*24+Morning+k,j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        Jan_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(Jan_Values)
#Feb values
Feb_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,28):
            temp=Raw_arr[(31*24)+i*24+Morning+k,j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        Feb_Values[k,j]=(sum/count)/Factor

print("###############################################################")
print(Feb_Values)
#March valuesJan_Values=np.empty([10,n_cols])
March_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,31):
            temp=Raw_arr[i*24+Morning+k+((31+28)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        March_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(March_Values)
#April Values
April_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,30):
            temp=Raw_arr[i*24+Morning+k+((31+28+31)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        April_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(April_Values)
#May values
May_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,31):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        May_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(May_Values)
#June values
June_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,30):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30+31)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        June_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(June_Values)

#July values
July_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,31):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30+31+30)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        July_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(July_Values)
#August values
Aug_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,31):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30+31+30+31)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        #print("k and count= ", k, count)
        Aug_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(Aug_Values)

#September values
Sep_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,30):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30+31+30+31+31)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        Sep_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(Sep_Values)

#October Values
Oct_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,31):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30+31+30+31+31+30)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        Oct_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(Oct_Values)
#November values
Nov_Values=np.empty([10,n_cols])
for k in range(0,Time_Range):
    for j in range(0,n_cols):
        count=0
        sum=0
        for i in range(0,30):
            temp=Raw_arr[i*24+Morning+k+((31+28+31+30+31+30+31+31+30+31)*24),j]
            if np.isnan(temp)==False:
                count+=1
                sum+=temp
        Nov_Values[k,j]=(sum/count)/Factor

print("count= ", count)
print("###############################################################")
print(Nov_Values)

#December value
# December data NOT AVAILABLE
Dec_Values=Nov_Values    #so till then we will use November data


# Dec_Values=np.empty([10,n_cols])
# for k in range(0,10):
#     for j in range(0,n_cols):
#         count=0
#         sum=0
#         for i in range(0,31):
#             temp=Raw_arr[i*24+8+k+((31+28+31+30+31+30+31+31+30+31+30)*24),j]
#             if np.isnan(temp)==False:
#                 count+=1
#                 sum+=temp
#         print("k,j= ", k,j)
#         print("count= ", count)
#         Dec_Values[k,j]=(sum/count)/Factor
#



row_list=[]
for i in range(0,Time_Range):
    row_list.append(i+Morning)

#Converting all the numpy array of each month to respective pandas dataframes

df1=pd.DataFrame(Jan_Values,columns=list,index=row_list)
df2=pd.DataFrame(Feb_Values,columns=list,index=row_list)
df3=pd.DataFrame(March_Values,columns=list,index=row_list)
df4=pd.DataFrame(April_Values,columns=list,index=row_list)
df5=pd.DataFrame(May_Values,columns=list,index=row_list)
df6=pd.DataFrame(June_Values,columns=list,index=row_list)
df7=pd.DataFrame(July_Values,columns=list,index=row_list)
df8=pd.DataFrame(Aug_Values,columns=list,index=row_list)
df9=pd.DataFrame(Sep_Values,columns=list,index=row_list)
df10=pd.DataFrame(Oct_Values,columns=list,index=row_list)
df11=pd.DataFrame(Nov_Values,columns=list,index=row_list)
df12=pd.DataFrame(Dec_Values,columns=list,index=row_list)


writer = pd.ExcelWriter(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\RawData.xlsx", engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='January')
df2.to_excel(writer, sheet_name='Feburary')
df3.to_excel(writer, sheet_name='March')
df4.to_excel(writer, sheet_name='April')
df5.to_excel(writer, sheet_name='May')
df6.to_excel(writer, sheet_name='June')
df7.to_excel(writer, sheet_name='July')
df8.to_excel(writer, sheet_name='August')
df9.to_excel(writer, sheet_name='September')
df10.to_excel(writer, sheet_name='October')
df11.to_excel(writer, sheet_name='November')
df12.to_excel(writer, sheet_name='December')

writer.save()




#
#
#
#
#
#
#
#
#
#
# print("###############################################################")
# print(Dec_Values)
