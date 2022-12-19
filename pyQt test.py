#py -m PyQt5.uic.pyuic -x t.ui -o t.py
import gc
gc.collect()
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem,QProgressBar

import psutil,datetime

from decimal import Decimal
from decimal import getcontext

import functools
from functools import reduce
from t import Ui_MainWindow
import sys

import numpy as np
import random
import time

import subprocess

def log(a,sel):
    sel.ui.textBrowser.append(str(a))

sys.set_int_max_str_digits(640000)



X=[]
l=0
flag=0
flag2=0



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.horizontalSlider.sliderReleased.connect(self.slide)

        self.setWindowTitle('САО массива')
        self.setWindowIcon(QtGui.QIcon("docs\icon256.png"))


        self.ui.label_15.setText(str(round(psutil.virtual_memory()[3]/1024**2))+' MB')
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')
        
        #кнопка Заполнить
        self.ui.pushButton_2.clicked.connect(self.Fill)
        #кнопка Вычислить
        self.ui.pushButton_3.clicked.connect(self.Calculate)
        #кнопка Удалить
        self.ui.pushButton_6.clicked.connect(self.Delete)
        #кнопка Автотест
        self.ui.pushButton_7.clicked.connect(self.Autotest)
        #кнопка Выход
        self.ui.pushButton_8.clicked.connect(self.Exit)
        #кнопка about
        self.ui.pushButton_9.clicked.connect(self.About)
        #кнока Обновить
        self.ui.pushButton_10.clicked.connect(self.Refresh)

    def Refresh(self): #Обновить монитор ресурсов
        self.ui.label_15.setText(str(round(psutil.virtual_memory()[3]/1024**2))+' MB')
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')





    def Autotest(self): #Автотест
        global l,X,flag,x1,x2
        if not flag: log("Ошибка: массив не задан",self)
        else:
            log('Автотест запущен',self)
            t_1=int(round(time.time() * 1000))
            log('Тест №1: проверка на количество элементов',self)
            t1=int(round(time.time() * 1000))
            if len(X)==l:
                t2=int(round(time.time() * 1000))
                T=t2-t1
                if T<1: log('   проверка выполнена успешно за <1 ms (массив сгенерирован полностью и имеет '+ str(l)+ ' элементов)',self)
                else: log('   проверка выполнена успешно за ' + str(T) +' ms',self)
            else:
                t2=int(round(time.time() * 1000))
                log('   проверка закончилась неудачей',self)
            
            
            
            log('Тест №2: проверка на сумму арифметической прогрессии',self)
            t1=int(round(time.time() * 1000))
            s=sum(X)
            S=((x1+x2)/2)*l
            t2=int(round(time.time() * 1000))
            T=t2-t1
            if T<1: log('   проверка выполнена успешно за <1 ms (s отличается от Sn на '+ str(round(abs(s/S-1)*100,1))+' %)',self)
            else: log('   проверка выполнена успешно за ' + str(T) +' ms (s отличается от Sn на '+ str(round(abs(s/S-1)*100,1))+' %)',self)

            


            log('Тест №3: проверка на диапазон',self)
            t1=int(round(time.time() * 1000))
            fl=0
            for i in range(l):
                if not(x1<=X[i] and X[i]<=x2+1):
                    fl=1
                    break
            t2=int(round(time.time() * 1000))
            if not(fl):
                T=t2-t1
                if T<1: log('   проверка выполнена успешно за <1 ms (каждый член массива входит в диапазон [' + str(x1)+','+str(x2)+'])',self)
                else: log('   проверка выполнена успешно за ' + str(T) +' ms (каждый член массива входит в диапазон [' + str(x1)+','+str(x2)+'])',self)
            else: log('   проверка закончилась неудачей',self)
            



            t_2=int(round(time.time() * 1000))
            T=t_2-t_1
            if T<1: log('Автотест закончен за <1ms',self)
            else: log('Автотест закончен за '+ str(T) +' ms',self)
            
            self.ui.label_15.setText(str(round(psutil.virtual_memory()[3]/1024**2))+' MB')
            self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')
        








    
    def Exit(self):
        self.close()
    def About(self):
        subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', 'Readme.txt'])
        






        
    def slide(self):
        self.ui.lineEdit.setText(str((self.ui.horizontalSlider.value()+1)*10000))
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')
        





    def Delete(self): #Удаление
        global l,X,flag,x1,x2
        X=[]
        flag=0
        self.ui.tableWidget.setColumnCount(0)
        self.ui.tableWidget.setRowCount(1)
        self.ui.lineEdit_5.setText(None)
        self.ui.progressBar.setValue(0)
        self.ui.label_9.setText("")
        
        self.ui.label_15.setText(str(round(psutil.virtual_memory()[3]/1024**2))+' MB')
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')
        











    def Fill(self): #Заполнить
        global X,flag,flag2,l,x1,x2
        flag=1
        leg=(self.ui.checkBox.checkState())

        self.ui.progressBar.setStyleSheet("QProgressBar{border-width: 5px;font: 8pt 'Google Sans';border-radius: 10px;border-color: beige;background-color: rgb(255, 255, 255);} QProgressBar:chunk{border-radius: 10px;background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(57, 182, 200, 255), stop:1 rgba(187, 255, 255, 255));}")
        
        self.ui.progressBar.setValue(0)
        self.ui.label_9.setText("")
        
        l = int(self.ui.lineEdit.text())
        x1,x2=float(self.ui.lineEdit_2.text()),float(self.ui.lineEdit_3.text())
        X=[0]*l
        

        log("Заполнение массива длинной "+str(l)+" c элементами от "+str(x1)+" до "+str(x2)+" начато...",self)

        t1=int(round(time.time() * 1000))

        self.ui.progressBar.setValue(0)
        self.ui.label_9.setText("")
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')
        
        if str(self.ui.comboBox_3.currentText())=="py.int": #Выбор метода заполнения массива
            x = np.random.randint(x1, x2+1, l,dtype=np.int64)
            X=[]
            for i in range(len(x)):
                X.append(int(x[i]))
                if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
                
        elif str(self.ui.comboBox_3.currentText())=="np.long":  
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="long")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.int_)
            
        elif str(self.ui.comboBox_3.currentText())=="np.short":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="short")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.short)
                
        elif str(self.ui.comboBox_3.currentText())=="np.int8":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="int8")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.int8)
                
                
        elif str(self.ui.comboBox_3.currentText())=="np.int16":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="int16")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.int16)
            
        elif str(self.ui.comboBox_3.currentText())=="np.int32":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="int32")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.int32)
            
        elif str(self.ui.comboBox_3.currentText())=="np.int64":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="int64")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.int64)
            
        elif str(self.ui.comboBox_3.currentText())=="np.longlong":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="longlong")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.longlong)
            
        elif str(self.ui.comboBox_3.currentText())=="np.ulonglong":
            x1,x2=int(x1),int(x2)+1
            if leg:
                X=np.zeros(l,dtype="ulonglong")
                for i in range(l):
                    X[i]=random.randint(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X=np.random.randint(x1, x2, l,dtype=np.ulonglong)
            
        elif str(self.ui.comboBox_3.currentText())=="py.float":
            #for i in range(len(X)):
            #    X[i]=random.uniform(x1, x2)
            if (self.ui.checkBox_2.checkState()):
                dec=int(self.ui.lineEdit_6.text())
                for i in range(l):
                    #X[i]=(str(Decimal(random.uniform(x1*10**dec, x2*10**dec))/Decimal(10**dec)))
                    if x1!=int(x1) or x2!=int(x2):
                        strl=str(random.uniform(x1,x2))
                        for j in range(dec//16):
                            n=str(random.uniform(0,1))[2:]
                            strl=strl+n
                    else:
                        strl=str(random.uniform(x1,x2))
                        for j in range(dec//16):
                            n=str(random.uniform(0,1))[2:]
                            strl=strl+n
                    X[i]=strl

                    if (i+1)%((l/100)+1)==0:
                        self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                for i in range(l):
                    X[i]=random.uniform(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                        self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар


            print(X[1],type(X[1]))
        elif str(self.ui.comboBox_3.currentText())=="np.float16":
            X=np.zeros(l,dtype="float16")
            for i in range(l):
                X[i]=random.uniform(x1, x2)
                if (i+1)%((l/100)+1)==0:
                    self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
                
        elif str(self.ui.comboBox_3.currentText())=="np.float32":
            X=np.zeros(l,dtype="float32")
            for i in range(l):
                X[i]=random.uniform(x1, x2)
                if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            
        elif str(self.ui.comboBox_3.currentText())=="np.float64":
            if leg:
                X=np.zeros(l,dtype="float64")
                for i in range(l):
                    X[i]=random.uniform(x1, x2)
                    if (i+1)%((l/100)+1)==0:
                            self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
            else:
                X = np.random.uniform(x1,x2,l)
            
        elif str(self.ui.comboBox_3.currentText())=="py.bin":
            X=np.random.choice([False, True], size=(l,), p=[1./3, 2./3])
            
        self.ui.progressBar.setValue(100)
        self.ui.label_9.setText("Завершено")
            



        size=sys.getsizeof(X)
        if size>1024**2:
            self.ui.lineEdit_5.setText(str(round(sys.getsizeof(X)/1024**2,3)))
            self.ui.label_13.setText('MB')
        elif size>1024:
            self.ui.lineEdit_5.setText(str(round(sys.getsizeof(X)/1024,3)))
            self.ui.label_13.setText('KB')
        else:
            self.ui.lineEdit_5.setText(str(sys.getsizeof(X)))
            self.ui.label_13.setText('Byte')
        


        
        
        if l>100 and not (self.ui.checkBox.checkState()): L,flag2=100,1
        else: L=l
        self.ui.tableWidget.setColumnCount(L)
        self.ui.tableWidget.setRowCount(1)
        for i in range(L):
            cellinfo = QTableWidgetItem(str(X[i]))
            self.ui.tableWidget.setItem(0, i, cellinfo)

            
        t2=int(round(time.time() * 1000))

        self.ui.label_9.setText("Завершено")
        self.ui.progressBar.setValue(100)
        self.ui.label_9.setText("Завершено")
        log("Массив длинной "+str(l)+" заполнен за "+str(t2-t1)+" ms",self)
        

        self.ui.label_15.setText(str(round(psutil.virtual_memory()[3]/1024**2))+' MB')
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')















        

    def Calculate(self): #Вычислить
        global l,X,flag,x1,x2
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setStyleSheet("QProgressBar{border-width: 5px;font: 8pt 'Google Sans';border-radius: 10px;border-color: beige;background-color: rgb(255, 255, 255);} QProgressBar:chunk{border-radius: 10px;background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(76, 200, 111, 255), stop:1 rgba(187, 255, 255, 255));}")
        self.ui.label_9.setText("")
        self.ui.textBrowser_2.setText("")

        getcontext().prec=int(self.ui.lineEdit_6.text())

        if not flag: log("Ошибка: массив не задан",self)
        else:
            if str(self.ui.comboBox.currentText())=="Сложение": #сложение
                log("Сложение "+str(len(X))+" элементов массива начато...",self)
                t1=int(round(time.time() * 1000))
                if type(X[0])==type(""):
                    s=Decimal(0)
                    for i in range(l):
                        s+=Decimal(X[i])
                else:
                    s=sum(X)
                t2=int(round(time.time() * 1000))
                if (t2-t1)<1: log(str(len(X))+" элементов были суммированы за <1 ms с результатом "+str(s),self)
                else: log(str(len(X))+" элементов были суммированы за "+str(t2-t1) +" ms с результатом "+str(s),self)
                self.ui.textBrowser_2.setText(str(s))
                self.ui.progressBar.setValue(100)



            elif str(self.ui.comboBox.currentText())=="Вычитание": #вычитание
                log("Вычитание "+str(len(X))+" элементов массива начато...",self)
                t1=int(round(time.time() * 1000))
                if type(X[0])==type(""):
                    s=Decimal(0)
                    for i in range(l):
                        s-=Decimal(X[i])
                else:
                    s=-sum(X)
                t2=int(round(time.time() * 1000))
                if (t2-t1)<1: log(str(len(X))+" элементов были вычтены за <1 ms с результатом "+str(s),self)
                else: log(str(len(X))+" элементов были вычтены за "+str(t2-t1) +" ms с результатом "+str(s),self)
                self.ui.textBrowser_2.setText(str(s))
                self.ui.progressBar.setValue(100)



            elif str(self.ui.comboBox.currentText())=="Умножение": #умножение
                log("Умножение "+str(len(X))+" элементов массива начато...",self)
                fl=0
                t1=int(round(time.time() * 1000))
                if 0 in X:
                    s=0
                    fl=1
                else:
                    #    s=reduce((lambda x, y: x * y), X)
                    if type(X[0])==type(""):
                        s=Decimal(1)
                        for i in range(l):
                            s*=Decimal(X[i])
                            if (i+1)%((l/100)+1)==0:
                                self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
                    else:
                        s=1.0
                        for i in range(l):
                            s*=X[i]
                            if (i+1)%((l/100)+1)==0:
                                self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
                        print(type(s))
                t2=int(round(time.time() * 1000))
                if len(str(s))>12: an=str(s)[:8]+"..."
                else: an=str(s)
                if s==0 and not fl:
                    if not 0 in X:
                        log("Ошибка: переполнение типа данных "+str(self.ui.comboBox_3.currentText()),self)
                        self.ui.textBrowser_2.setText("Ошибка")
                else:
                    if (t2-t1)<1:
                        log(str(len(X))+" элементов были перемножены за <1 ms с результатом "+an,self)
                    else:
                        log(str(len(X))+" элементов были перемножены за "+str(t2-t1) +" ms с результатом "+an,self)
                    self.ui.textBrowser_2.setText(str(Decimal(s)))
                    print(Decimal(s))
                



            elif str(self.ui.comboBox.currentText())=="Деление": #деление
                log("Деление "+str(len(X))+" элементов массива начато...",self)
                
                if 0 in X:
                    log("Ошибка: деление на ноль",self)
                    self.ui.textBrowser_2.setText("Ошибка")
                
                else:
                    t1=int(round(time.time() * 1000))
                    if type(X[0])==type(""):
                        s1=Decimal(1)
                        
                        for i in range(l):
                            s1*=Decimal(X[i])
                            if (i+1)%((l/100)+1)==0:
                                self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
                        s=Decimal(1)/Decimal(s1)
                    else:
                        s1=0
                        for i in range(l):
                            s1*=X[i]
                            if (i+1)%((l/100)+1)==0:
                                self.ui.progressBar.setValue(int((i)/(l/100))+1) #прогресс бар
                        s=1/s1

                    t2=int(round(time.time() * 1000))
                    if len(str(s))>12: an=str(s)[:8]+"..."
                    else: an=str(s)
                    if (t2-t1)<1: log(str(len(X))+" элементов были поделены за <1 ms с результатом "+an,self)
                    else: log(str(len(X))+" элементов были поделены за "+str(t2-t1) +" ms с результатом "+an,self)
                    if s==0 and 0 not in X:
                        self.ui.textBrowser_2.setText('1/'+str(s1))
                    else:
                        self.ui.textBrowser_2.setText(str(Decimal(s)))
                        print(Decimal(s))
                




            elif str(self.ui.comboBox.currentText())=="Умножить на...": #Умножить на...
                mn=int(self.ui.lineEdit_4.text())
                log("Умножение на "+str(mn)+" каждого элемента массива начато...",self)
                t1=int(round(time.time() * 1000))
                if type(X[0])==type(""):
                    for i in range(l):
                        X[i]=Decimal(X[i])*Decimal(mn)
                        cellinfo = QTableWidgetItem(str(X[i]))
                        self.ui.tableWidget.setItem(0, i, cellinfo)
                else:
                    for i in range(len(X)):
                        X[i]=X[i]*mn
                        cellinfo = QTableWidgetItem(str(X[i]))
                        self.ui.tableWidget.setItem(0, i, cellinfo)
                
                t2=int(round(time.time() * 1000))
                
                
                if (t2-t1)<1: log(str(len(X))+"элементов массива были домножены на "+str(mn)+" за <1 ms",self)
                else: log(str(len(X))+" элементов массива были домножены на " +str(mn)+" за "+str(t2-t1) +" ms",self)
                self.ui.textBrowser_2.setText("См. таблицу")
                self.ui.progressBar.setValue(100)
                




            elif str(self.ui.comboBox.currentText())=="Возведение в ... степень": #Возведение
                mn=int(self.ui.lineEdit_4.text())
                log(str(mn),self)
                log("Возведение в "+str(mn)+" степень каждого элемента массива начато...",self)
                t1=int(round(time.time() * 1000))
                
                if type(X[0])==type(""):
                    for i in range(l):
                        X[i]=Decimal(X[i])**Decimal(mn)
                        cellinfo = QTableWidgetItem(str(X[i]))
                        self.ui.tableWidget.setItem(0, i, cellinfo)
                else:
                    for i in range(len(X)):
                        X[i]=X[i]**mn
                        cellinfo = QTableWidgetItem(str(X[i]))
                        self.ui.tableWidget.setItem(0, i, cellinfo)
                
                t2=int(round(time.time() * 1000))
                
                
                if (t2-t1)<1: log(str(len(X))+"элементов массива были возведены в "+str(mn)+" степень за <1 ms",self)
                else: log(str(len(X))+" элементов массива были возведены в " +str(mn)+" степень за "+str(t2-t1) +" ms",self)
                self.ui.textBrowser_2.setText("См. таблицу")
                



                
        self.ui.progressBar.setValue(100)
        self.ui.label_9.setText("Завершено")
        self.ui.label_15.setText(str(round(psutil.virtual_memory()[3]/1024**2))+' MB')
        self.ui.label_17.setText(str(int(psutil.cpu_freq().current))+' Mhz')
            
        
        

   
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())