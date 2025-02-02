import pandas as pd
import numpy as np

class LinearRegression():

    def __init__(self):
        self.coef =None
        self.intercept = None

    def fit(self, X_train, y_train):
        X_train = np.insert(X_train,0,1,axis=1)

        betas = np.linalg.inv(np.dot(X_train.T,X_train)).dot(X_train.T).dot(y_train)


        self.coef = betas[1:]
        self.intercept = betas[0]


    def predict(self, X_test):
        y_pred = self.intercept + np.dot(X_test, self.coef)

        return y_pred



from sklearn.datasets import load_diabetes


X,y = load_diabetes(return_X_y=True)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 2)

lr = LinearRegression()

lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

print(predictions)
