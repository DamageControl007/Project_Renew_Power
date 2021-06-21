import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


PDS=pd.ExcelFile("RawData.xlsx")
anisotropy=pd.ExcelFile("All_anisotropy_values.xlsx")
df_g=pd.read_excel(anisotropy,2)
df_number=pd.read_excel(PDS,  0)
list=df_number.columns.values.tolist()
list.pop(0)
print(list)

Hulu=df_g.to_numpy()

Time1=Hulu[1].tolist()
Time1.pop(0)

# Time2=Hulu[3].tolist()
# Time2.pop(0)
#
# Time3=Hulu[5].tolist()
# Time3.pop(0)

plt.plot(list,Time1, color='b')
# plt.plot(list,Time2, color='b', label='11:00 AM')
# plt.plot(list,Time3, color='g', label='1:00 PM')
plt.xlabel("diameter (in nm)")
plt.ylabel("Anisotropy values")
plt.title("RI= 1.5")
plt.legend()
plt.show()
