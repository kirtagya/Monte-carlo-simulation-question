# birthday paradox
import statistics
import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
Ymean = []#null list used for plot graph
NumList = []
for num in range(100,1000):# loop on num from 100 to 1000
    runLength = []
    for i in range(num):
        Bday = []
        while True:
            day = random.randint(1, 365)
            if day in Bday:
                break # break when repeatation of number occur while taking random number (1,365)
            #print(day,Bday)
            Bday.append(day)
        runLength.append(len(Bday))
    print(statistics.mean(runLength))
    Ymean.append(statistics.mean(runLength))
    
    NumList.append(num)
plt.plot(NumList,Ymean)
plt.show()







