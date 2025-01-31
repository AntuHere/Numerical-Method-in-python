import pandas as pd
import numpy as np

## We Will train the data by fitting and predict the data


"""
y = mX + b
we will find the best m and b value

Creating an Object for Simple Linear Regression

1. Fit()
this is main algorithm to train the data 
2. Predict()
this is for the prediction after training

#--------------------------------------#
we can also use scikit learn for this-

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit()
lr.predict()
"""

class LinearRegression:
    def __init__(self):
        self.m = None
        self.b = None
    
    def fit(self,X_train, y_train):
        num = 0
        den = 0
        
        for i in range(X_train.shape[0]):
           
            num = num + ((X_train[i] - X_train.mean()) * (y_train[i] - y_train.mean()))
            den += ((X_train[i] - X_train.mean()) *(X_train[i] - X_train.mean())) 
        
        self.m = num / den
        self.b = y_train.mean() - (self.m * X_train.mean())
        
        print(self.m)
        print(self.b)

    def predict(self, X_test):
        return self.m * X_test + self.b


file = r'F:\Python\ML\Linear Regression\placement.csv'
df = pd.read_csv(file)

# print(df.head())


X = df.iloc[:,0].values
y = df.iloc[:,1].values


## This is optional just splitting tha data into train and tese
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)



## Fit the data or train the data 
lr = LinearRegression()
lr.fit(X_train,y_train)

## Prediction using the class object predict()
print(lr.predict(X_test))





