from sklearn.tree import DecisionTreeRegressor
import numpy as np
from math import *

def func(x1,x2):
    return x1*2.0-3.0*x2

numSamples = 100
X = np.random.rand(numSamples,2)
Y = np.zeros(numSamples)
for i in range(numSamples):
    Y[i] = func(X[i][0],X[i][1])

clf = DecisionTreeRegressor()
clf = clf.fit(X,Y)

X_test = np.random.rand(10,2)
Y_test = np.zeros(10)
for i in range(10):
    Y_test[i] = func(X_test[i][0],X_test[i][1])
    pred = clf.predict([X_test[i]])[0]
    print(pred,Y_test[i],abs(pred-Y_test[i]))
