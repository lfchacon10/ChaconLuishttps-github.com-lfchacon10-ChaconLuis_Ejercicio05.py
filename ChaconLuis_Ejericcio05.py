import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

datos='cssccs'
caras=0
sellos=0

for char in datos:
    if(char=='s'):
        sellos=+1
    elif(char=='c'):
        caras=+1
        
print( "Caras ",caras, " Sellos", sellos)

#Ns=caras
#Nc=sellos
Ns=7
Nc=5


H=np.linspace(0,1,1000)

prior =np.ones(1000)



pCara= H
pSello= H-1

pCpS= (H**Nc)*(1-H)**Ns


plt.plot(H,pCpS)

delta= (np.max(H)- np.min(H))/len(H)
print (delta)

pObs= integrate.simps( pCpS, H)*delta

print(pObs)



