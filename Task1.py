import pandas as pd
import numpy as np
import seaborn as sns

dataset = pd.read_excel('QVI_transaction_data.xlsx')
dataset.head()

dataset.describe()#summaries the data

dataset.isnull().sum()#outlier

sns.boxplot(dataset.TOT_SALES)

sns.displot(dataset.TOT_SALES, kde = True)#after 600 outlier

#removing outlier mean from 7.3

numericdata = dataset.select_dtypes(['float','int'])

numericdata.head()

x = numericdata[numericdata['TOT_SALES']<8.00]
#removed

sns.distplot(x.TOT_SALES,  kde= True )
#checking result reoved outlier
sns.boxplot(x.TOT_SALES)

#checking dataset
dataset.dtypes









