# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:23:26 2019

@author: Parth
"""
def traintest():

    '''
    # face detection 
    from os import listdir
    from os.path import isdir
    from PIL import Image
    from matplotlib import pyplot
    from numpy import savez_compressed
    from numpy import asarray
    from mtcnn.mtcnn import MTCNN
    from numpy import load
    from numpy import expand_dims
    from keras.models import load_model
    
    
    
    
    
    
    # extract a single face from a given photograph
    def extract_face(filename, required_size=(160, 160)):
        # load image from file
        image = Image.open(filename)
        # convert to RGB
        image = image.convert('RGB')
        # convert to array
        pixels = asarray(image)
        # create the detector, using default weights
        detector = MTCNN()
        # detect faces in the image
        results = detector.detect_faces(pixels)
        
        # extract the bounding box from the first face
        x1, y1, width, height = results[0]['box']
        # bug fix
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        # extract the face
        face = pixels[y1:y2, x1:x2]
        # resize pixels to the model size
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array = asarray(image)
        return face_array
    
    # load images and extract faces for all images in a directory
    def load_faces(directory):
        faces = list()
        # enumerate files
        for filename in listdir(directory):
            # path
            path = directory + filename
            # get face
            face = extract_face(path)
            # store
            faces.append(face)
        return faces
    
    
    
    
    
    
    
    def embed(classroom):
        
        classroom=classroom
        print("class",classroom)
        # get the face embedding for one face
        
        def get_embedding(model, face_pixels,classroom):
            # scale pixel values
            face_pixels = face_pixels.astype('float32')
            
            mean, std = face_pixels.mean(), face_pixels.std()
            face_pixels = (face_pixels - mean) / std
            # transform face into one sample
            samples = expand_dims(face_pixels, axis=0)
            # make prediction to get embedding
            yhat = model.predict(samples)
            return yhat[0]
        allow_pickle=True
        # load the face dataset
        #div=input("Enter your division")
        train=classroom+'.npz'
        
        data = load(train)
        #print(train)
        #print("data=",data['arr_0'])
        #print("data2=",data['arr_1'])
        test=classroom+'-test.npz'
        #print(test)
        data1=load(test)
        #print("data3=",data1['arr_0'])
        #print("data4=",data1['arr_1'])
        
        
        trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data1['arr_0'], data1['arr_1']
        print('Loaded: ', trainX.shape, trainy.shape, testX.shape, testy.shape)
        # load the facenet model
        
        model = load_model('facenet_keras.h5')
        print('Loaded Model')
        # convert each face in the train set to an embedding
        newTrainX = list()
        for face_pixels in trainX:
            embedding = get_embedding(model, face_pixels,classroom)
            newTrainX.append(embedding)
        newTrainX = asarray(newTrainX)
        #print(newTrainX.shape)
        # convert each face in the test set to an embedding
        newTestX = list()
        for face_pixels in testX:
            embedding = get_embedding(model, face_pixels,classroom)
            newTestX.append(embedding)
        newTestX = asarray(newTestX)
        #print(newTestX.shape)
        # save arrays to one file in compressed format
        savez_compressed(classroom+'-embedding.npz', newTrainX, trainy, newTestX, testy)
        #print(newTrainX, trainy, newTestX, testy)
        embed='be6'+'-embedding.npz'
        data = load(embed)
        print("Embed=",embed)
        trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
        print(trainy)
    
    
    
    
    
    
    
    
    
    # load a dataset that contains one subdir for each class
    def load_dataset(directory):
        X, y = list(), list()
        # enumerate folders, on per class
        #print(directory)
        print(directory)
        for subdir in listdir(directory):
            classroom=subdir
            directory=directory+'/'+classroom
            print("dir",directory)
            for subdir in listdir(directory):
                # path
                #classroom=subdir
                print("subdir=",subdir)
                path = directory +'/'+subdir + '/'
                print("path=",path)
                #skip files in dir
                
                if not isdir(path):
                    continue
                # load all faces in the subdirectory
                faces = load_faces(path)
                # create labels
                labels = [subdir for _ in range(len(faces))]
                # summarize progress
                print('>loaded %d examples for class: %s' % (len(faces), subdir))
                # store
                X.extend(faces)
                y.extend(labels)
                savez_compressed(classroom+"-test.npz",X,y)
                print("inside loaddata")
                directory='E:/OneDrive/val'
                print(classroom)
                embed(classroom)
    
    
    p='E:/OneDrive/val'
    print(p)
    load_dataset(str(p))
    print("data trained")
    '''
    
    
    return "test trained"

def bcd():
    
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
    def delete():
        uid=int(input("Enter the uid to delete"))
        y=str(input("Enter year"))
        d=str(input("Enter div"))
        #c.execute('DELETE FROM students WHERE Reg_No=(?)',(uid,))
        var=("DELETE FROM students WHERE Reg_No=%s")
        var2=(uid,)
        c.execute(var,var2)
        conn.commit()
        conn.close()
        parent_dir="E:/FaceRec/students/train/"+str(y)+str(d)
        path=os.path.join(parent_dir,str(uid))
        shutil.rmtree(path)
    inp=int(input("Enter 1 to delete and 2 to create"))
    
    
    if(inp==1):
        delete()
    elif(inp==2):
        
        def registration():
            
            #print(app.li)
            name=str(input("Enter your name"))
            reg_no=int(input("Enter your registration number "))
            
            division=int(input("Enter division "))
            roll_no=int(input("Enter your roll number"))
            year=str(input("Enter your year "))
            phone_no=int(input("Enter your phone number"))
            print(name,year)
            #c.execute('INSERT INTO students (Name,Reg_No,Year,Div,Roll_No,Phone_No) VALUES (?,?,?,?,?,?)',(name,reg_no,year,division,roll_no,phone_no))
            
            var=("INSERT INTO students"
                 "(Name,Reg_No,Year,Roll_No,Phone_No,Division)"
                 " VALUES (%s,%s,%s,%s,%s,%s)")
            var2=(name,reg_no,year,roll_no,phone_no,division)
            c.execute(var,var2)
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
    else:
        print()
    cap.release()
    conn.commit()
    conn.close()
    
    cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    return "dataset trained"
    