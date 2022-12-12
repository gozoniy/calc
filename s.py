from decimal import *
from random import *
getcontext().prec = 6
print(Decimal(1) / Decimal(7))

getcontext().prec = 1000
X=[]
for i in range(1000):
    X.append(uniform(0.999, 1.001))
print(X[1])
s=(Decimal(1))
for i in range(1000):
    s*=Decimal(X[i])
print(Decimal(s))
