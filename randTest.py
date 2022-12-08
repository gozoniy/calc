from random import randint
import time,functools
from functools import reduce
from itertools import accumulate

import numpy as np

x1,x2=map(int,input().split())
l=int(input())
X=[0]*l
for i in range(l):
    X[i]=(randint(x1,x2))
#     if i%(l/10)==0: print(int(i/(l/100)),"%")
t1=int(round(time.time() * 1000))
# X = list(numpy.random.randint(1,15, size=l))
x = np.random.randint(x1, x2, size=l, dtype=np.int32)
# x=np.random.uniform(x1, x2, l,dtype='float32')
# x = np.random.normal(1e7).astype('float16')
# x = np.empty(l, dtype=np.float16)
# x = np.random.default_rng()
# x.standard_normal(5, dtype=np.float32)

# x=np.array([1.2, 2, 3], dtype='float64')
# x=np.arange(0.5,5.0,0.5)

# for i in range(len(x)):
#     X.append(int(x[i]))

# X = np.array([10],dtype='int64')

t2=int(round(time.time() * 1000))
if (t2-t1)<1:print("<1 ms")
else: print(t2-t1,"ms")
# print(len(items), items[:5])  # 100000 [73846 49707 18846 73887 43349]

print(X,"...")
print(X)
key=input("key? ")
if key=="+":
    
    s=sum(X)
    t2=int(round(time.time() * 1000))
    if (t2-t1)<1:print("<1 ms")
    else: print(t2-t1,"ms")

elif key=="-":
    t1=int(round(time.time() * 1000))
    s=0
    for i in range(len(X)):
        s-=X[i]
        if i%(l/10)==0: print(int(i/(l/100)),"%")
    t2=int(round(time.time() * 1000))
    print(t2-t1,"ms")
    
elif key=="*":
    t1=int(round(time.time() * 1000))
#     s=(functools.reduce(lambda a, b : a * b, X))
#     s=reduce((lambda x, y: x * y), X)
#     s=list(accumulate(X, (lambda x, y: x * y)))
    s=(functools.reduce(lambda a, b : a * b, X))
    t2=int(round(time.time() * 1000))
    print(t2-t1,"ms",s)
    
elif key=="/":
    t1=int(round(time.time() * 1000))
    s=1.0000001
    for i in range(len(X)):
        s/=X[i]
        if i%(l/10)==0: print(int(i/(l/100)),"%")
    t2=int(round(time.time() * 1000))
    print(t2-t1,"ms")