import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import random
numList = []
winRate = []
win_switchRate=[]
for num in range(100,1000):
    # define the initializing of variable 
    win_switch=0
    lose_switch=0
    win=0
    sim_no=0
    lose=0
    for k in range(num):
        doors =["goat","car","goat"]
        sim_no=sim_no+1
        #print("simulation number"+ str(sim_no))
        random.shuffle(doors)
        #print(doors)
        #  if we switch the door winning probability
        n=random.randrange(3)
        if doors[n]=="car":#first choice is car
            lose_switch=lose_switch+1#because u change the choice
            #print("goat")
        if doors[n]=="goat":
            win_switch=win_switch+1
            #print("car")
        # if without swiching the door winning probability
        if doors[n]=="car":#first choice is car
            win=win+1#because u did not change the choice
            #print("car")
        if doors[n]=="goat":
            lose=lose+1
            #print("goat")    
    s=win*100/num
    d=win_switch*100/num
    #print(num,win,lose)
    print(s)
    print(d)
    numList.append(num)
    winRate.append(s)
    win_switchRate.append(d)
plt.plot(numList,winRate)
plt.show()
plt.plot(numList,win_switchRate)
plt.show()
