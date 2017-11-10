#AJH
#Sample code for blog:
#Yields basic information about data repository 
#prior to machine learning analysis

import pandas as pd
import matplotlib as mplt

def surveyData(data_url, columns)
   #Access data, apply titles
   data = pd.read_csv(data_url, names=columns)
   #find rows and columns
   print(data.shape)
   #check data structure
   print(data.head(3))
   #find missing values
   print(data.isnull().sum())
   #categorize
   print(data.groupby('Sex').size())
   #statistics
   print(data.describe())
   #Histograms
   data.hist()
   mplt.show()
   #Correlation plots
   scatter_matrix(data)
   mplt.show()

#set target
data_url = "https://archive.ics.uci.edu/ml/
           machine-learning-databases/abalone/abalone.data"
#set titles                                                          
columns = ['Sex','Length','Diameter','Height','WholeWeight', 
           'ShuckedWeight', 'VisceraWeight', 'ShellWeight', 'Rings']
#pass target and titles to surveyData and run the program                                     
surveyData(data_url, columns)
