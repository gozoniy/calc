import time
import random
import numpy
import math
from functools import reduce
import decimal
from tqdm import tqdm

def zapolnenie():
    global a,a2,vvod2,c,c1,c2
    print("Выберите тип элементов массива: 1 - int64, 2 - long, 3 - float, 4 - long double")
    vvod2 = input()
    if vvod2=='1':
        print("С какого числа:")
        c1=int(input())
        print("До какого числа:")
        c2=int(input())
        print("Количество:")
        c = int(input())
        start = time.time()
        a = list(numpy.random.randint(c1,c2+1, size=c))
        a = numpy.array(a, dtype=numpy.int64)
        a2 = [int(x) for x in a]
        end = time.time()
        print("Заполнение массива инт64 :", (end-start), "s")
    elif vvod2=='2':
        print("С какого числа:")
        c1=int(input())
        print("До какого числа:")
        c2=int(input())
        print("Количество:")
        c = int(input())
        start = time.time()
        a = list(numpy.random.randint(c1,c2+1, size=c))
        a = numpy.array(a, dtype=numpy.compat.long)
        a2 = [int(x) for x in a]
        end = time.time()
        print("Заполнение массива лонг :", (end-start), "s")
    elif vvod2=='3':
        print("С какого числа:")
        c1=float(input())
        print("До какого числа:")
        c2=float(input())
        print("Количество:")
        c = int(input())
        start = time.time()
        a = list(numpy.random.uniform(c1,c2, size=c))
        a = numpy.array(a, dtype=numpy.float64)
        a2 = [float(x) for x in a]
        end = time.time()
        print("Заполнение массива вещ :", (end-start), "s")
    elif vvod2=='4':
        print("С какого числа:")
        c1=float(input())
        print("До какого числа:")
        c2=float(input())
        print("Количество:")
        c = int(input())
        start = time.time()
        a = list(numpy.random.uniform(c1,c2, size=c))
        a = numpy.array(a, dtype=numpy.longdouble)
        a2 = [float(x) for x in a]
        end = time.time()
        print("Заполнение массива вещ :", (end-start), "s")

def test_zapol():
    for i in range(5):
        zapolnenie()

def summa():
    global b
    start = time.time()
    b = sum(a2)
    end = time.time()
    print(b)
    print("Время поиска суммы :", (end-start), "s")
    
def test_summa():
    start_avg = time.time()
    for i in tqdm(range(5)):
        summa()
    end_avg = time.time()
    print('\x1b[6;30;42m' + "Среднее время поиска суммы :", (end_avg-start_avg)/5, "s" + '\x1b[0m')

    

def nesumma():
    global b
    start = time.time()
    b = a2[0] - sum(a2) + a2[0]
    end = time.time()
    print(b)
    print("Время поиска вычитания :", (end-start), "s")
    
def test_nesumma():
    start_avg = time.time()
    for i in tqdm(range(5)):
        nesumma()
    end_avg = time.time()
    print('\x1b[6;30;42m' + "Среднее время поиска вычитания :", (end_avg-start_avg)/5, "s" + '\x1b[0m')
    
def proizv():
    b = 1
    start = time.time()
    for i in tqdm(range(len(a2))):
        b*=a2[i]
    end = time.time()
    x22 = str('{:.1000f}'.format(b))
    print(x22)
    for j in range(1000,0,-1):
        if x22[j]=='0':
            x22=x22[:j]
        else:
            print(x22)
            break
    print("Время поиска произведения :", (end-start), "s")

def test_proizv():
    start_avg = time.time()
    for i in tqdm(range(5)):
        proizv()
    end_avg = time.time()
    print('\x1b[6;30;42m' + "Среднее время поиска произведения :", (end_avg-start_avg)/5, "s" + '\x1b[0m')
    

def delen():
    b = a2[0]
    bb = 0
    start = time.time()
    for i in tqdm(range(1,len(a2))):
        b=b/a2[i]
        bb = b
        bb = math.nextafter(bb, -math.inf)
    end = time.time()
    print(bb)
    print("Время поиска деления :", (end-start), "s")

def test_delen():
    start_avg = time.time()
    for i in tqdm(range(5)):
        delen()
    end_avg = time.time()
    print('\x1b[6;30;42m' + "Среднее время поиска деления :", (end_avg-start_avg)/5, "s" + '\x1b[0m')


def stepen():
    start = time.time()
    b = 1
    for i in tqdm(range(1,len(a2))):
        b*=a2[i]
    b = (a2[0]**(b))
    print(b)
    end = time.time()
    print("Время поиска степени :", (end-start), "s")
    
def test_stepen():
    start_avg = time.time()
    for i in tqdm(range(5)):
        stepen()
    end_avg = time.time()
    print('\x1b[6;30;42m' + "Среднее время поиска деления :", (end_avg-start_avg)/5, "s" + '\x1b[0m')    

def test1():
    if c==len(a2):
        print("test1 +")
    else:
        print("test1 -")

def test2():
    if max(a2)<=c2 and min(a2)>=c1:
        print("test2 +")
    else:
        print("test2 -")
    print(max(a2),min(a2))
    
prog = "run"
x22=0
while prog != "stop":
    print("1 - создать массив, 2 - сумма, 3 - вычитание, 4 - произведение, 5 - деление, 6 - показать список, "+ '\x1b[7;31;47m' +"7 - стоп"+ '\x1b[0m' +", 8 - тест суммы, 9 - тест вычитания, 10 - тест произведения, 11 - тест деления, 12 - степень, 13 - тест степени, 14 - автотест")
    vvod = input()
    if vvod=='1':
        zapolnenie()
    elif vvod=='2':
        summa()
    elif vvod=='3':
        nesumma() 
    elif vvod=='4':
        proizv()
    elif vvod=='5':
        delen()
    elif vvod=='6':
        for i in range(len(a)):
            x22 = str('{:.1000f}'.format(a[i]))
            for j in range(1000,0,-1):
                if x22[j]=='0':
                    x22.replace(x22[j],'')
            print(a[i])
    elif vvod=='7':
        prog == "stop"
        break
    elif vvod=='8':
        test_summa()
    elif vvod=='9':
        test_nesumma()
    elif vvod=='10':
        test_proizv()
    elif vvod=='11':
        test_delen()
    elif vvod=='12':
        stepen()
    elif vvod=='13':
        test_stepen()
    elif vvod=='14':
        test1()
        test2()