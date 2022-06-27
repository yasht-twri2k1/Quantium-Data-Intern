import pandas as pd
import numpy as np

dataset = pd.read_csv('QVI_data.csv')
dataset.head()
#total sales
total_sales = sum(dataset['TOT_SALES'])
print(total-sales)

#average customer

#There is not any customer column in dataset but we can get
#customer by TX_ID,because it is unique for every individual

#total customer =241
dataset.describe()

#Total_customer =241584

#average number of transaction per customer

dataset.shape()

avg_trns = Total_customer/2648384

print(avg_trns)
#0.912209






