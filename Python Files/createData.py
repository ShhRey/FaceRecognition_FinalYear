# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:57:11 2019

@author: Parth
"""
def createdata(name,reg_no,year,roll_no,phone_no,division):
    import cv2
    import numpy as np 
    import sqlite3
    import os
    import shutil
    import mysql.connector
    from mysql.connector import Error
    from os import listdir
    

    def connect():
        try:
            conn=mysql.connector.connect(host="remotemysql.com",database="Q1xhwcVnZF",user="Q1xhwcVnZF",password="a83LzHFIbd")
            if conn.is_connected():
                print("Connected")
        except Error as e:
            print(e)
    if __name__=='__main__':
        connect()

    conn=mysql.connector.connect(host="remotemysql.com",database="Q1xhwcVnZF",user="Q1xhwcVnZF",password="a83LzHFIbd")
    c=conn.cursor()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    #database="attendance.db"

    #conn=sqlite3.connect(database)
    #c=conn.cursor()

    list1=[]
    

    def registration():

        #print(app.li)
        #name=str(input("Enter your name"))
        #reg_no=int(input("Enter your registration number "))

        #division=int(input("Enter division "))
        #roll_no=int(input("Enter your roll number"))
        #year=str(input("Enter your year "))
        #phone_no=int(input("Enter your phone number"))
        #print(name,year)


        var=("INSERT INTO students"
             "(Name,Reg_No,Year,Roll_No,Phone_No,Division)"
             " VALUES (%s,%s,%s,%s,%s,%s)")
        print("var=",var)
        print("bss=",name,reg_no,division,roll_no,year,phone_no)
        var2=(name,reg_no,year,roll_no,phone_no,division)
        c.execute(var,var2)
        print("2")

        division2=str(division)
        print(division2)

        var3=("INSERT INTO "+year+division2+"t"+"(UID)"
              " VALUES (%s)")
        print("var3=",var3)

        var4=(reg_no,)
        c.execute(var3,var4)


        return reg_no,division,year
    reg_no,div,year=registration()
    reg_no=str(reg_no)
    p="E:/FaceRec/students/train/"
    #print("p=",p)
    for folders in listdir(p):
        #print(folders)
        list1.append(folders)
    f=str(year)+str(div)
    if f not in list1:
        #print(f)
        npi=p+f
        #print(np)
        os.mkdir(npi)

    parent_dir="E:/FaceRec/students/train/"+str(year)+str(div)
    print("parent=",parent_dir)
    path = os.path.join(parent_dir, reg_no)
    print("path=",path)
    os.mkdir(path)
    store=parent_dir+'/'+reg_no+'/'
    print("store",store)
    sampleNum=0





    while True:


        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #print("While loop")
        for (x,y,w,h) in faces:
            #print(sampleNum)
            sampleNum = sampleNum+1
            #print(sampleNum)
            img_name="User."+str(sampleNum)+".jpg"
            #print(img_name)
            cv2.imwrite(str(store)+str(img_name), gray[y:y+h,x:x+w])
            print(str(store)+str(img_name))
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            #cv2.waitKey(100)
        cv2.imshow('img',img)
        key=cv2.waitKey(10);
        if key==27:
            break
        elif sampleNum>17:
            break
    
    cap.release()
    conn.commit()
    conn.close()

    cv2.destroyAllWindows()
    
    return "Data created"
