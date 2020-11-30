# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import math
from scipy.stats import pearsonr

fexcel=pd.read_csv(open('EIVP_KM.csv'),sep=';')
date_tableau=fexcel['sent_at'].tolist()
temperature=fexcel['temp'].tolist()
humidite=fexcel['humidity'].tolist()
lum=fexcel['lum'].tolist()
CO2=fexcel['co2'].tolist()
num_capteur=fexcel['id'].tolist()


date=[]
for i in range(len(date_tableau)):
    date.append(datetime.strptime(date_tableau[i],'%Y-%m-%d %H:%M:%S%z'))


temperature1=[]
for i in range(len(temperature)):
    if num_capteur[i]==1:
        temperature1.append(temperature[i])

date1=[]
for i in range(len(date)):
    if num_capteur[i]==1:
        date1.append(date[i])

humidite1=[]
for i in range(len(humidite)):
    if num_capteur[i]==1:
        humidite1.append(1/humidite[i])

lum1=[]
for i in range(len(lum)):
    if num_capteur[i]==1:
        lum1.append(lum[i])

co2_1=[]
for i in range(len(CO2)):
    if num_capteur[i]==1:
        co2_1.append(CO2[i])

x = date1
y = temperature1
w=humidite1
v=lum1
z=co2_1

plt.plot(x,y)

plt.title('Evolution de la température en fonction du temps')
plt.xlabel('temps')
plt.ylabel('temperature')
#plt.gcf().autofmt_xdate()
plt.show()
plt.close()

def min(liste):
    m=liste[0]
    for i in range(len(liste)):
        if m>liste[i]:
            m=liste[i]
    return m

def maxi(liste):
    m=liste[0]
    for i in range(len(liste)):
        if m<liste[i]:
            m=liste[i]
    return m

def moy(liste):
    s=0
    for i in range(len(liste)):
        s=s+liste[i]
    return s/len(liste)

def var(liste):
    m=moy(liste)
    v=0
    for k in range(0,len(liste)):
        v=v+(liste[k]-m)**2
    return(v/len(liste))

def ecart_type(liste):
    return var(liste)**(1/2)


def tri(liste):
    if liste==[]:
        return []
    pivot=liste.pop()
    p,g,e=[],[],[pivot]
    for x in liste:
        if x<pivot:
            p.append(x)
        elif x>pivot:
            g.append(x)
        else:
            e.append(x)
    return tri(p)+e+tri(g)

def mediane(liste):
    list=tri(liste)
    if len(list)%2==0:
        a=len(list)//2
        return (list[a-1]+list[a])/2
    else:
        return len(list)/2



def humidex(humidite,temp):
    H=[]
    for i in range(len(temp)):
        H.append(temp[i]+(5/9)*(6.112*(10**(7.5*(temp[i]/(237.7+temp[i])))*(humidite[i]/100))-10))
    return H


def idc(x,y):
    moy_x=moy(x)
    moy_y=moy(y)
    difprod=0
    xdiff2=0
    ydiff2=0
    for i in range(len(x)):
        xdiff=x[i]-moy_x
        ydiff=y[i]-moy_y
        xdiff2+=xdiff*xdiff
        ydiff2+=ydiff*ydiff
        difprod+=xdiff*ydiff
    return difprod/math.sqrt(xdiff2*ydiff2)


coeff_pearson=pearsonr(temperature1,humidite1)[0]
print(coeff_pearson)
print(idc(temperature1,humidite1))








