import numpy as np
import pandas as pd
import miepython as mp


col=129
row=10
n_comp=4
def Normalized(RawData, row, col):
    Total=np.array([])
    Total=RawData.sum(axis=1)
    print("sum of rows: ", Total)
    for i in range(0, row):
        print("Value of Total[", i, "]=", Total[i])
        for j in range(0, col-2):
            RawData.iat[i,j+2]=RawData.iat[i,j+2]/Total[i]
    print("The normalized distribution is below: ")
    print("sum of normalized: ", RawData.sum(axis=1))

def Area(dia):
    return np.pi*(dia/2)**2

def Extinction_coeff(dia,n_comp):
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
        #anisotropy(dia,i,ans[3])
    return Qext

def Interaction_coeff(rows, cols, n_comp):
    Ut=[]
    cm=10000000
    frac=[0.05,0.55,0.1,0.3]
    for j in range(0,cols):
        dia=RawData.columns[j+2]/cm
        Qx=Extinction_coeff(dia,n_comp)
        A=Area(dia)
        Ut.append([])
        for i in range(0,rows*(n_comp)):
            if (i%(n_comp)==0):
                num=RawData.iat[int(i/(n_comp)),j+2]
            Ut[j].append(Qx[i%(n_comp)]*A*frac[i%(n_comp)]*num)
    return Ut

def transpose(l1):
    l2=[]
    # we have nested loops in comprehensions
    # value of i is assigned using inner loop
    # then value of item is directed by row[i]
    # and appended to l2
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2



Ut_file=np.array([np.array([0 for i in range(0,col-2)]) for j in range(0,row)])
#Keep it here for future reference
#newSheet = np.array([ np.array([ 0 for i in range(col)]) for j in range(row)])
print(Ut_file)

FileName="RawData1.xlsx"
RawData=pd.read_excel(FileName)
print(RawData)
print('Elements of df', RawData.iat[0,2])
Normalized(RawData, row, col)
Ut=Interaction_coeff(row,col,n_comp)
Ut=transpose(Ut)
print(Ut)
list=RawData.columns.values.tolist()
list.pop(0)
list.pop(0)
df = pd.DataFrame(Ut,columns=list)
print(df)
df.to_excel("Ut_values.xlsx")
print("AFter normalization")
Area(0)
