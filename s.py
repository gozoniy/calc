from decimal import *
from random import *

getcontext().prec = 100
X=[]
for i in range(1000):
    X.append(uniform(0.9, 1.1))
print(X[1])
s=(Decimal(1))
for i in range(1000):
    s*=Decimal(X[i])
print(Decimal(s))
dec=100
for i in range(100) :
    X.append(str(Decimal(uniform(1*10**dec, 5*10**dec))/Decimal(10**dec)))
print('s=',X[1])
p=Decimal(1)
for i in range(100):
    p*=Decimal(X[i])
print('p=',p)
