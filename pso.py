'''
pso.py
A simple implementation of the Particle Swarm Optimisation Algorithm.
Uses Numpy for matrix operations. 
'''
import timeit
import csv
import sys
import numpy as np
from numpy import array
from random import random
from math import sin, sqrt
import matplotlib.pyplot as plt
import matplotlib.pylab as pp

a=[]
b=[]
a1=[]
b1=[]
c1=[]
c2=[]
m1=[]
m2=[]
l=1
m=1

def initialize():
    with open("candy1.csv", "rb") as f:
        reader = csv.reader(f)
        data=list(reader)
    for i in data:
        k=float(i[0])
        a.append(k)
        k=float(i[1])
        b.append(k)
initialize()
iter_max = 3
pop_size = len(a)
c1 = 2
c2 = 2
err_crit = 0.00001

#empty class

class Particle:
    pass
        

def f6(param):
    '''Schaffer's F6 function'''
    para = param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
        (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
    denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
            (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
    f6 =  0.5 - (num/denom)
    errorf6 = 1 - f6
    return f6, errorf6;
    
        
    
start = timeit.default_timer() 
#initialize the particles
ar=[]
particles = []
for i in range(pop_size):
    ar=[]
    p = Particle()          #object creation
    #p.params = array([random() for i in range(2)])
    ar.append(a[i])
    ar.append(b[i])
    p.params=array(ar)
    p.fitness = 0.0
    p.v = 0.0
    particles.append(p)
    


# let the first particle be the global best
gbest = particles[0]
err = 999999999
i=0
while i < iter_max :
    for p in particles:
        fitness,err = f6(p.params)
        if fitness > p.fitness:
            p.fitness = fitness
            p.best = p.params

        if fitness > gbest.fitness:
            gbest = p
        v = p.v + c1 * random() * (p.best - p.params) \
                + c2 * random() * (gbest.params - p.params)
        p.params = p.params + v
          
    i  += 1
    if err < err_crit:
        break
    #progress bar. '.' = 10%
    #if i % (iter_max/10) == 0:
    #    print '.'
stop = timeit.default_timer()
time1=stop - start 
print time1


pr=[]
qr=[]
lst=[]
for i in range(0,pop_size):
    if(particles[i].params[0]>=0 and particles[i].params[1]>=0):
        pr.append(particles[i].params[0])
        qr.append(particles[i].params[1])  
for i in range(0,len(pr)):
    lst.append([pr[i],qr[i]])


'''
mat=np.matrix(lst)
plt.scatter(mat[:,0],mat[:,1],color='blue')
'''

#print 'pso',time1
with open("output3.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(lst)


execfile('pso and kmeans.py')
print time1+stop-start
