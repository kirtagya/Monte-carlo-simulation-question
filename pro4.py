import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statistics
import numpy as np
NumList = []
ansList = []
#Nsim = 10000
for num in range(100,1000):

    for i in range(num):
        u= stats.uniform.rvs(0,1,size=num)
        x=u*10+2
        y = []
        for x1 in x:
            y.append(min(x1,10))

        #print(statistics.mean(y))
    ansList.append(statistics.mean(y))
    NumList.append(num)
plt.plot(NumList,ansList)
plt.show()



