import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Filename="RawData.xlsx"
NumConentration=pd.ExcelFile(Filename)
df=pd.read_excel(NumConentration,0)

list=df.columns.values.tolist()
list.pop(0)
print(list)
df_g=df.to_numpy()
df_Lol=np.delete(df_g[3], 0)
print(df_Lol)
df_mass=[]

plt.plot(list,df_Lol,color='red')
plt.xlabel("Diameter (in nm)")
plt.ylabel("Number per cm3")
plt.title("Particle size distribution on January at 11:00 AM")
plt.legend()
plt.show()

for i in range(0, len(list)):
    val=(4/3)*(np.pi)*((list[i]*pow(10,-7)/2)**(3))*df_Lol[i]*1.5*pow(10,12)
    df_mass.append(val)
print("Total mass= ", sum(df_mass))

plt.plot(list, df_mass, color='blue')
plt.xlabel("Diameter (in nm)")
plt.ylabel("Concentration in ug/m3")
plt.title("Particle mass distribution on January at 11:00 AM")
plt.legend()
plt.show()
