import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import random
import matplotlib.pyplot as plt
from math import *


def myFunc(x):
    out1 = x[0]**2-x[1]*0.5*x[2]
    out2 = x[0]*1.1/x[1]+x[2]
    return out1,out2


numSamples = 1000
x_train = np.zeros([numSamples,3])
y_train = np.zeros([numSamples,2])
xs = np.zeros(numSamples)
ys = np.zeros(numSamples)
for i in range(numSamples):
    x_train[i][0] = random.random()*10.0
    x_train[i][1] = random.random()*10.0
    x_train[i][2] = random.random()*10.0
    xs[i],ys[i] = myFunc(x_train[i])
    y_train[i][0],y_train[i][1] = xs[i],ys[i]

plt.scatter(xs,ys,c='black',marker='+')
#regr_1 = DecisionTreeRegressor(max_depth=2)
#regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=34)
#regr_1.fit(x_train, y_train)
#regr_2.fit(x_train, y_train)
regr_3.fit(x_train, y_train)

'''
x_test = np.zeros([numNewPoints,3])
y_test = np.zeros([numNewPoints,2])
for i in range(len(x_test)):
    x_test[i][0] = random.random()*10.0
    x_test[i][1] = random.random()*10.0
    x_test[i][2] = random.random()*10.0
    y_test[i][0],y_test[i][1],y_test[i][2],y_test[i][3] = myFunc(x_test[i])
print(x_test,y_test)

y_1 = regr_1.predict(x_test)
y_2 = regr_2.predict(x_test)
y_3 = regr_3.predict(x_test)
print(y_test)
print(y_3)
'''

# want points around [1.0,2.0]+-tol
tol = 2.0
numNewPoints = 50
numAccepted = 0
x_test = np.zeros([numNewPoints,3])
y_test = np.zeros([numNewPoints,2])
xs = np.zeros(numNewPoints)
ys = np.zeros(numNewPoints)
while numAccepted < numNewPoints:
  x1 = random.random()*10.0
  x2 = random.random()*10.0
  x3 = random.random()*10.0
  xx = np.asarray([[x1,x2,x3]])
  yy = regr_3.predict(xx)
  if (abs(yy[0][0]-7.0)<=tol) and (abs(yy[0][1]-12.0)<=tol):
    x_test[numAccepted] = xx
    xs[numAccepted] = yy[0][0]
    ys[numAccepted] = yy[0][1]
    print(xs[numAccepted],ys[numAccepted],xx)
    numAccepted += 1
plt.plot(xs,ys,"ro")
xs = np.zeros(numNewPoints)
ys = np.zeros(numNewPoints)
for i in range(numNewPoints):
  xs[i],ys[i] = myFunc(x_test[i])
plt.scatter(xs,ys,c='blue',marker='s')
plt.xlim(-10,20)
plt.ylim(-10,20)
plt.show()