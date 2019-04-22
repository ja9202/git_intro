from matplotlib import pyplot as plt
import pandas as pd

data1=pd.read_csv('D:/Material/VBA/noise.csv')
#print(data1)
noise_data_filter=data1.Valeo_first_check=='Noise'
noise=data1[noise_data_filter]

seized_data_filter=data1.Valeo_first_check=='Seized'
seized=data1[seized_data_filter]

CB_data_filter=data1.Valeo_first_check=='Center bolt loosen'
CB=data1[seized_data_filter]

plt.scatter(CB.Registration_date, CB.Mileage_km,label='CB',color='green',marker='*')
plt.scatter(seized.Registration_date, seized.Mileage_km,label='seized',color='blue')
plt.legend(['CB','seized'])
plt.show()