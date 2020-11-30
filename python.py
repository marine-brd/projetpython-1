# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
NICOLAS
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import math
from scipy.stats import pearsonr

"CREATION DE LISTES"
fexcel=pd.read_csv(open('EIVP_KM.csv'),sep=';')
noise=fexcel['noise'].tolist()
date_tableau=fexcel['sent_at'].tolist()
temperature=fexcel['temp'].tolist()
humidite=fexcel['humidity'].tolist()
lum=fexcel['lum'].tolist()
CO2=fexcel['co2'].tolist()
num_capteur=fexcel['id'].tolist()

"LECTURE DES DATES PAR PYTHON"
date=[]
for i in range(len(date_tableau)):
    date.append(datetime.strptime(date_tableau[i],'%Y-%m-%d %H:%M:%S%z'))

"CAPTEUR 1"
date1=[]
for i in range(len(date)):
    if num_capteur[i]==1:
        date1.append(date[i])
noise1=[]
for i in range(len(noise)):
    if num_capteur[i]==1:
        noise1.append(noise[i])
temp1=[]
for i in range(len(temperature)):
    if num_capteur[i]==1:
        temp1.append(temperature[i])
hum1=[]
for i in range(len(humidite)):
    if num_capteur[i]==1:
        hum1.append(1/humidite[i])
lum1=[]
for i in range(len(lum)):
    if num_capteur[i]==1:
        lum1.append(lum[i])        
co2_1=[]
for i in range(len(CO2)):
    if num_capteur[i]==1:
        co2_1.append(CO2[i])               

"CAPTEUR 2"       
date2=[]
for i in range(len(date)):
    if num_capteur[i]==2:
        date2.append(date[i])
noise2=[]
for i in range(len(noise)):
    if num_capteur[i]==2:
        noise2.append(noise[i])
temp2=[]
for i in range(len(temperature)):
    if num_capteur[i]==2:
        temp2.append(temperature[i])
hum2=[]
for i in range(len(humidite)):
    if num_capteur[i]==2:
        hum2.append(1/humidite[i])        
lum2=[]
for i in range(len(lum)):
    if num_capteur[i]==2:
        lum2.append(lum[i])        
co2_2=[]
for i in range(len(CO2)):
    if num_capteur[i]==2:
        co2_2.append(CO2[i])        
 
"CAPTEUR 3"       
date3=[]
for i in range(len(date)):
    if num_capteur[i]==3:
        date3.append(date[i]) 
noise3=[]
for i in range(len(noise)):
    if num_capteur[i]==3:
        noise3.append(noise[i])
temp3=[]
for i in range(len(temperature)):
    if num_capteur[i]==3:
        temp3.append(temperature[i])
hum3=[]
for i in range(len(humidite)):
    if num_capteur[i]==3:
        hum3.append(1/humidite[i])        
lum3=[]
for i in range(len(lum)):
    if num_capteur[i]==3:
        lum3.append(lum[i])
co2_3=[]
for i in range(len(CO2)):
    if num_capteur[i]==3:
        co2_3.append(CO2[i])

"CAPTEUR 4"        
date4=[]
for i in range(len(date)):
    if num_capteur[i]==4:
        date4.append(date[i])   
noise4=[]
for i in range(len(noise)):
    if num_capteur[i]==4:
        noise4.append(noise[i])
temp4=[]
for i in range(len(temperature)):
    if num_capteur[i]==4:
        temp4.append(temperature[i])
hum4=[]
for i in range(len(humidite)):
    if num_capteur[i]==4:
        hum4.append(1/humidite[i])        
lum4=[]
for i in range(len(lum)):
    if num_capteur[i]==4:
        lum4.append(lum[i])
co2_4=[]
for i in range(len(CO2)):
    if num_capteur[i]==4:
        co2_4.append(CO2[i])

"CAPTEUR 5"        
date5=[]
for i in range(len(date)):
    if num_capteur[i]==5:
        date5.append(date[i]) 
noise5=[]
for i in range(len(noise)):
    if num_capteur[i]==5:
        noise5.append(noise[i])
temp5=[]
for i in range(len(temperature)):
    if num_capteur[i]==5:
        temp5.append(temperature[i])
hum5=[]
for i in range(len(humidite)):
    if num_capteur[i]==5:
        hum5.append(1/humidite[i])        
lum5=[]
for i in range(len(lum)):
    if num_capteur[i]==5:
        lum5.append(lum[i])
co2_5=[]
for i in range(len(CO2)):
    if num_capteur[i]==5:
        co2_5.append(CO2[i])

"CAPTEUR 6"      
date6=[]
for i in range(len(date)):
    if num_capteur[i]==6:
        date6.append(date[i])  
noise6=[]
for i in range(len(noise)):
    if num_capteur[i]==6:
        noise6.append(noise[i])
temp6=[]
for i in range(len(temperature)):
    if num_capteur[i]==6:
        temp6.append(temperature[i])
hum6=[]
for i in range(len(humidite)):
    if num_capteur[i]==6:
        hum6.append(1/humidite[i])        
lum6=[]
for i in range(len(lum)):
    if num_capteur[i]==6:
        lum6.append(lum[i])
co2_6=[]
for i in range(len(CO2)):
    if num_capteur[i]==6:
        co2_6.append(CO2[i])


"CALCULS MATHEMATIQUES"
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


"COMPARAISON"
print(moy(temp1)) 
print(moy(temp2))
print(moy(temp3))
print(moy(temp4))
print(moy(temp5))
print(moy(temp6))

print(moy(noise1)) 
print(moy(noise2))
print(moy(noise3))
print(moy(noise4))
print(moy(noise5))
print(moy(noise6))

print(moy(hum1)) 
print(moy(hum2))
print(moy(hum3))
print(moy(hum4))
print(moy(hum5))
print(moy(hum6))

print(moy(lum1)) 
print(moy(lum2))
print(moy(lum3))
print(moy(lum4))
print(moy(lum5))
print(moy(lum6))

print(moy(co2_1)) 
print(moy(co2_2))
print(moy(co2_3))
print(moy(co2_4))
print(moy(co2_5))
print(moy(co2_6))


print(ecart_type(temp1)) 
print(ecart_type(temp2))
print(ecart_type(temp3))
print(ecart_type(temp4))
print(ecart_type(temp5))
print(ecart_type(temp6))

print(ecart_type(noise1)) 
print(ecart_type(noise2))
print(ecart_type(noise3))
print(ecart_type(noise4))
print(ecart_type(noise5))
print(ecart_type(noise6))

print(ecart_type(hum1)) 
print(ecart_type(hum2))
print(ecart_type(hum3))
print(ecart_type(hum4))
print(ecart_type(hum5))
print(ecart_type(hum6))

print(ecart_type(lum1)) 
print(ecart_type(lum2))
print(ecart_type(lum3))
print(ecart_type(lum4))
print(ecart_type(lum5))
print(ecart_type(lum6))

print(ecart_type(co2_1)) 
print(ecart_type(co2_2))
print(ecart_type(co2_3))
print(ecart_type(co2_4))
print(ecart_type(co2_5))
print(ecart_type(co2_6))







#print(idc(temperature2,humidite2))
#
#coeff_pearson=pearsonr(temperature2,humidite2)[0]
#print(coeff_pearson)

x=date
y=temperature

w=hum1
v=lum1
z=co2_1

plt.plot(x,y)
plt.title('Evolution de la température en fonction du temps')
plt.xlabel('temps')
plt.ylabel('temperature')
#plt.text(2,20,"min=")
plt.show()
plt.close()

def anomalie(liste):
    L=[]
    m=moy(liste)
    e_c=ecart_type(liste)
    for i in range(len(liste)):
        if liste[i]<m-3*e_c:
            L.append(liste[i])
        elif liste[i]>m+3*e_c:
            L.append(liste[i])
    return L








