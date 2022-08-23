import statistics
import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


Xvals = [ -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 ]
Ymean = []
Yvar = []
NumList = []
for num in range(100,1000):
    Yvals = []
    for i in range(num):
        Yvals.append(abs(random.choice(Xvals)))
    print(statistics.mean(Yvals), statistics.pvariance(Yvals))
    Ymean.append(statistics.mean(Yvals))
    Yvar.append(statistics.pvariance(Yvals))
    NumList.append(num)

plt.plot(NumList,Ymean)
plt.show()