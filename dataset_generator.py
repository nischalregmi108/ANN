'''
Basic dataset generators studying ANN
Based on:
    Simon Haykin, Neural Networks and Learning Machines
'''

import numpy as np
import math

def generate_half_moon(nPoints_by_2, radius, width, distance):
    x = np.zeros([2*nPoints_by_2,2])
    label =[]
    for i in range(nPoints_by_2):
        R = radius + np.random.uniform(-width/2,width/2)
        theta = np.random.uniform(0,math.pi)
        x[i,0] = R*math.cos(theta)
        x[i,1] = R*math.sin(theta)
        label.append(0)
    for i in range(nPoints_by_2,2*nPoints_by_2):#generate point for the lower half
        R = radius + np.random.uniform(-width/2,width/2)
        theta = np.random.uniform(0,math.pi)
        x[i,0] = R*math.cos(theta)
        x[i,1] = R*math.sin(theta)
        x[i,1] = -x[i,1] #reflect along y-axis
        x[i,1] -= distance #translate along y-axis
        x[i,0] += radius #translate along x-axis
        label.append(1)
    return x, label

def start():
    x,label = generate_half_moon(1000, 10, 6, -5)
    import matplotlib.pyplot as plt
    plt.scatter(x[:,0],x[:,1], c=label)
    plt.show()
    
    
if __name__ == "__main__":
        start()