import glob
import math
import random
import timeit
import csv
import numpy as np
import matplotlib.pyplot as plt
import csv

centroids=[]
a=[]
b=[]
c1=[]
c2=[]
m1=[]
m2=[]
l=1
m=1
name="output3.csv"
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
root = Tk()
k=tkSimpleDialog.askinteger("Prompt Box","Enter no of clusters")
root.destroy()
def initialize():
    fp=open(name,"r")
    data=fp.readlines()
    for i in data:
        s=""
        pos=0
        for j in range(0,len(i)):
            if(i[j]!=','):
                s=s+i[j]
            else:
                pos=j
                break
        f=float(s)
        a.append(f)
        s=""
        for j in range(pos+1,len(i)):
            if(i[j]!='\n'):
                s=s+i[j]
            else:
                break
        f=float(s)
        b.append(f)
   
def centroid(k):
    centroids=random.sample(range(len(a)),k)
    return centroids
'''
    
lst=[]  
l=[]         
def centroid(k):
    x=0
    y=0
    for i in range(0,len(a)):
       x=x+a[i]
       y=y+b[i]
    for i in range(0,len(a)):
        lst.append([Eucledian(x,y,a[i],b[i]),i])
    lst.sort(reverse=True)
    c=k
    prev=0
    i=0
    while(c>0):
        if(prev!=lst[i]):  
            prev=lst[i]
            l.append(prev)
            i=i+1
            c=c-1
    for i in l:
        centroids.append(i[1])
    return centroids
'''

#mean=cluster mean
mean=[]           
flag=1


def clusters():
    for i in centroids:
        mean.append([a[i],b[i]])
    for i in range(0,len(a)):
        sum1=0
        sum2=0
        flag=1
        mean1=[]
        for j in range(0,len(centroids)):        
            if (i==centroids[j]):
                flag=0
        if(flag==0):
            flag=1
        else:
            for j in range(0,len(centroids)):    
                mean1.append(Eucledian(mean[j][0],mean[j][1],a[i],b[i]))
            c=mean1.index(min(mean1))
            cluster[c].append(i)
            for j in cluster[c]:
                sum1=sum1+a[j]
                sum2=sum2+b[j]
            mean[c][0]=sum1/len(cluster[c])
            mean[c][1]=sum2/len(cluster[c])
            
                
def Eucledian(a,b,c,d):
    sum=0
    sum=sum+math.pow((a-c),2);
    sum=sum+math.pow((b-d),2);
    sum=math.sqrt(sum);
    return sum;
 
def iteration():
    flag=1
    for i in range(0,len(centroids)):
        length_cluster=len(cluster[i])
        j=0
        while(j<length_cluster):
            mean1=[]
            sum1=0
            sum2=0
            for k  in range(0,len(centroids)):
                mean1.append(Eucledian(mean[k][0],mean[k][1],a[cluster[i][j]],b[cluster[i][j]]))
            c=mean1.index(min(mean1))
            if(i!=c):
                flag=0
                cluster[c].append(cluster[i][j])
                del cluster[i][j]
                length_cluster=length_cluster-1
                for m in cluster[i]:
                    sum1=sum1+a[m]
                    sum2=sum2+b[m]
                mean[i][0]=sum1/len(cluster[i])
                mean[i][1]=sum2/len(cluster[i])
                sum1=0
                sum2=0
                for m in cluster[c]:
                    sum1=sum1+a[m]
                    sum2=sum2+b[m]
                mean[c][0]=sum1/len(cluster[c])
                mean[c][1]=sum2/len(cluster[c])
            j=j+1
    return flag
      
                    
initialize()
cluster=[]
centroids=centroid(k)
pos=centroids[1]
start = timeit.default_timer()
for i in centroids:
    cluster.append([i])
clusters()
flag=0
while(flag==0):
    flag=iteration()


stop = timeit.default_timer()


c=0
col=['aqua','yellow','darkgrey','lightgreen','lightblue','pink','salmon','khaki','orange','plum']
for i in cluster:
    mat=[]
    for j in i:
        mat.append([a[j],b[j]])
    mat=np.matrix(mat)
    plt.scatter(mat[:,0],mat[:,1],color=col[c])
    c=c+1
plt.show()
#print stop-start