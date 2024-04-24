import numpy as np
from applications.models import songs,Users
import flask_sqlalchemy
from sqlalchemy import or_
import random 

def findL(a,b):
    d = songs.query.filter(or_(songs.Genre == a, songs.Genre == b)).all()
    h=Users.query.filter(Users.type=='creator').all()
    Y_train=[]
    F={}
    k=0
    for i in h:
        F[i.name]=k
        k=k+1
    for i in d:
        y=[]
        y.append(i.id)
        y.append(F[i.Artist])
        y.append(i.Albumid)
        Y_train.append(y)
    
    means=[]
    means.append(Y_train[0])
    means.append(Y_train[1])
    means.append(Y_train[2])

    #initial box assignment
    ans= assignCluster(Y_train,means)
    datak1 = []
    datak2 = []
    datak3 = []

    for i in range(len(Y_train)):
        if ans[i] == 0:
            datak1.append(Y_train[i])
        elif ans[i] == 1:
            datak2.append(Y_train[i])
        elif ans[i] == 2:
            datak3.append(Y_train[i])
    datak1 = np.array(datak1)
    datak2 = np.array(datak2)
    datak3 = np.array(datak3)

    means= compute_cluster_centers(datak1,datak2,datak3)
    for i in range(10):
        ans= assignCluster(Y_train,means)
        dataak1 = []
        dataak2 = []
        dataak3 = []

        for i in range(len(Y_train)):
            if ans[i] == 0:
                dataak1.append(Y_train[i])
            elif ans[i] == 1:
                dataak2.append(Y_train[i])
            elif ans[i] == 2:
                dataak3.append(Y_train[i])
        datak1 = np.array(dataak1)
        datak2 = np.array(dataak2)
        datak3 = np.array(dataak3)
        means= compute_cluster_centers(datak1,datak2,datak3)
    
    datak1x= datak1.tolist()
    datak3x= datak3.tolist()
    datak2x= datak2.tolist()

    for i in datak1x:
        i.pop()
        i.pop()
    flatteneddatak1 = []
    [flatteneddatak1.extend(inner) for inner in datak1x]

    for i in datak2x:
        i.pop()
        i.pop()
    flatteneddatak2 = []
    [flatteneddatak2.extend(inner) for inner in datak2x]

    for i in datak3x:
        i.pop()
        i.pop()
    flatteneddatak3 = []
    [flatteneddatak3.extend(inner) for inner in datak3x]

    final=[]
    final.append(flatteneddatak1)
    final.append(flatteneddatak2)
    final.append(flatteneddatak3)
    return final


def compute_cluster_centers(datak1,datak2,datak3):
  m=[]
  m.append(np.mean(datak1, axis=0))
  m.append(np.mean(datak2, axis=0))
  m.append(np.mean(datak3, axis=0))
  return m

def assignCluster(X,Cmean): #X=Ytrain Cmean=means
    Z=[]
    for v in X:
        min= 1000000000000
        newv = v[1:] 
        newv=np.array(newv)
        for i in range(3):
            newCmeani=Cmean[i][1:]
            newCmeani=np.array(newCmeani)
            distance= np.linalg.norm(newv - newCmeani, ord=2)
            if distance<min:
                min=distance
                got=i
        Z.append(got)
    return Z
    
    #use k means make list of list where inner list = songs id outer list = list of such clusters