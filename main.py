import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('lamborghini_sales_2020_2025.csv')
colors_array = ["#0c0116","#5c6bff"]
labels_array = ['Gasoline','Hybrid']

HP = df['Horsepower']

FT = df.groupby(df['Fuel Type']).size()
print(FT)

fig, ax = plt.subplots()
fig.set_facecolor('#F8F9FA')
ax.pie(FT,colors=colors_array,labels=labels_array,autopct='%1.1f%%',textprops= {
'color' : '#F8F9FA'
})
plt.title("Fuel Type of Lamborghini cars sold from 2020-2025")
plt.show()