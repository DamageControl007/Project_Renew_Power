import numpy as np
import pandas as pd
import miepython as mp






def ProcessData(row, col, n_comp,list,df_num):
    Normal=Normalized(row, col,df_num)
    Ut=Interaction_coeff(row,col,n_comp,Normal,list)
    Ut=transpose(Ut)
    df= pd.DataFrame(Ut,columns=list)
    print("df")
    print(df)
    return df



def Excel(df_list,file,sheet,itr):
    writer = pd.ExcelWriter(file+".xlsx", engine='xlsxwriter')
    for i in range(0,itr):
        # Write each dataframe to a different worksheet.
        df_list[i].to_excel(writer, sheet_name=sheet[i])
    writer.save()


def Normalized( rows, cols,df_num):
    Normal=RawData[df_num].to_numpy()
    Total=Normal.sum(axis=1)
    print("sum of rows: ", Total)
    for i in range(0, rows):
        print("Value of Total[", i, "]=", Total[i])
        for j in range(0, cols):
            Normal[i,j+1]=Normal[i,j+1]/Total[i]
    print("The normalized distribution is below: ")
    print("sum of normalized: ", Normal.sum(axis=1))
    return Normal

def Area(dia):
    return np.pi*(dia/2)**2

def Anisotropy(dia,g,i,j):
    g_factor[i][j]=g

def Extinction_coeff(dia,n_comp,j):
    Qext=[]
    N_re=1                                                                        # Real part of RI of medium(water in this case)
    N_im=0                                                                        # Imaginary part of RI of water
    N=complex(float(N_re),float(N_im))
    n_comp=4                                                                      # Number of components in air
    M_re=[1.57, 1.5, 1.38,1.6]                                                    # Real part of particle R.I
    M_im=[0.53,0,0,0]
    M=[]
    for i in range(0,n_comp):
        M.append(complex(float(M_re[i]),float(-M_im[i])))

    cm=10000000                                                          # Imaginary part of particle R.I
    wavl=550/cm
    X=(3.14*dia*N_re)/wavl
    for i in range(0,n_comp):
        ans=mp.mie(M[i],X)
        Qext.append(ans[0])
        Anisotropy(dia,ans[3],i,j)
    return Qext

def Interaction_coeff(rows, cols, n_comp, Normal,list):
    Ut=[]
    cm=10000000
    frac=[0.05,0.55,0.1,0.3]
    for j in range(0,cols):
        dia=list[j]/cm
        Qx=Extinction_coeff(dia,n_comp,j)
        A=Area(dia)
        Ut.append([])
        for i in range(0,rows*(n_comp)):
            if (i%(n_comp)==0):
                sum=0
                num=Normal[int(i/(n_comp)),j+1]
            temp=Qx[i%(n_comp)]*A*frac[i%(n_comp)]*num
            sum+=temp
            Ut[j].append(temp)
            if (i%(n_comp)==n_comp-1):
                Ut[j].append(sum)
    return Ut

def transpose(l1):
    l2=[]
    # we have nested loops in comprehensions
    # value of i is assigned using inner loop
    # then value of item is directed by row[i]
    # and appended to l2
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2
def Cumulative(df_list,sheets,months,list):
    global rows,cols
    print("rawdata: ")
    df_cumulative=[]
    for k in range(0,months):
        cum_val=RawData[k].to_numpy()
        cum_val=np.delete(cum_val,0,axis=1)
        Total=cum_val.sum(axis=1)
        #cum_val=np.delete(cum_val,0,axis=1)
        print(cum_val)
        for i in range(0,rows):
            sum=0
            for j in range(0,cols):
                sum+=cum_val[i,j]/Total[i]
                cum_val[i,j]=sum
        print("RAWDATA=", cum_val)
        df_cumulative.append(pd.DataFrame(cum_val,columns=list))

    Excel(df_cumulative, r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\Cumulative_values",sheet,months)




FileName=(r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\RawData.xlsx")
xls = pd.ExcelFile(FileName)
temp=pd.read_excel(xls, 0)
rows,cols=temp.shape
cols=cols-1
n_comp=4
list=temp.columns.values.tolist()
Ut_file=np.array([np.array([0 for i in range(0,cols-2)]) for j in range(0,rows)])
#Keep it here for future reference
#newSheet = np.array([ np.array([ 0 for i in range(col)]) for j in range(row)])
print(Ut_file)
list[0]="Time"
temp_list=list
temp_list.pop(0)
list2=temp_list
print(list)
sheet=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
months=12
RawData=[]
df_list=[]
df_g=[]
for i in range(0,months):
    print("i=", i)
    g_factor=np.zeros((n_comp, cols))
    RawData.append(pd.read_excel(xls, i))
    df_list.append(ProcessData(rows,cols,n_comp,list,i))
    print("g_factor")
    df_g.append(pd.DataFrame(g_factor,columns=list2))
    print(df_g[i])


Excel(df_list,r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\All_UT_values",sheet,months)
Excel(df_g,r"G:\OneDrive - IIT Delhi\Courses\Sem8\MTP CLD880\New Codes in Jupyter\Final excel files\All_anisotropy_values",sheet,months)
Cumulative(df_list,sheet,months,list)

# RawData=pd.read_excel(FileName)
# print(RawData)
# print('Elements of df', RawData.iat[0,2])
# Normalized(RawData, row, col)
# Ut=Interaction_coeff(row,col,n_comp)
# Ut=transpose(Ut)
# print(Ut)
# list=RawData.columns.values.tolist()
# list.pop(0)
# list.pop(0)
# df = pd.DataFrame(Ut,columns=list)
# print(df)
# df.to_excel("Ut_values.xlsx")
# print("AFter normalization")
# Area(0)
