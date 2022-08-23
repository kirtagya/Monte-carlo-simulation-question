import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statistics
import numpy as np


#num = 100
NumList = []
ansList = []
for num in range(100,1000):
    total19000 = 0
    for i in range(num):
        men = stats.uniform.rvs(0,1,size=300)
        x = men*75+25
        weightSum = sum(x)

        if weightSum > 19000:
            total19000 = total19000 + 1

    print(total19000/num)
    ansList.append(total19000/num)
    NumList.append(num)
plt.plot(NumList,ansList)
plt.show()