

def rec(serial,yr,day):

    from os import listdir
    import mysql.connector
    from mysql.connector import Error


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



    list1=[]
    list2=[]
    directory="E:/FaceRec/students/train"
    directory2="E:/OneDrive/val"
    for folder in listdir(directory):
        #print(folder)
        list1.append(folder)
    #print(list1)

    for folder in listdir(directory2):
        list2.append(folder)
    #print(list2)




    """
    Created on Fri Sep 13 23:07:55 2019

    @author: Parth
    """

    # classification
    from random import choice
    from numpy import load
    from numpy import expand_dims
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import Normalizer
    from sklearn.svm import SVC
    from matplotlib import pyplot
    import sqlite3

    #database="attendance.db"
    #conn=sqlite3.connect(database)
    #c=conn.cursor()
    atten=[]
    #serial=0
    #time=float(input("Enter approx time in decimal"))
    #yr=(input("Enter year and div"))
    #day=input("Enter day")
    '''
    if time>=10 and time<11:
        serial=2
        int(serial)
        str(yr)
        str(day)
    elif time>=11 and time<12:
        serial=3
        int(serial)
        str(yr)
        str(day)
    
    elif time>=13 and time<14:
        serial=5
        int(serial)
        str(yr)
        str(day)
    elif time>=14 and time<15:
        serial=6
        int(serial)
        str(yr)
        str(day)
    elif time>=15 and time<16:
        serial=7
        int(serial)
        str(yr)
        str(day)
    elif time>=16 and time<17:
        serial=8
        int(serial)
        str(yr)
        str(day)
    '''
    print("serialllll=",serial,yr,day)
    # load faces
    #div=input("Enter your division")
    for values in list1:
        for values2 in list2:
            if(values==values2):
                count=0
                div=values
                print(div)
                test="E:/flask/"+div+'-test.npz'
                #test="E:/FaceRec/be6-test.npz"
                #print(test)
                data = load(test)
                #print("data=",data)
                testX_faces = data['arr_0']
                #print("test=",testX_faces)
                # load face embeddings
                if len(testX_faces)!=0:

                    embed="E:/flask/"+div+'-embedding.npz'
                    data = load(embed)
                    #print("Embed=",embed)
                    trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
                    # normalize input vectors
                    #print("trainy1",trainy,trainX)
                    in_encoder = Normalizer(norm='l2')
                    trainX = in_encoder.transform(trainX)
                    testX = in_encoder.transform(testX)
                    # label encode targets
                    out_encoder = LabelEncoder()
                    out_encoder.fit(trainy)
                    trainy = out_encoder.transform(trainy)
                    testy = out_encoder.transform(testy)
                    # fit model
                    #print("trainy",trainy)
                    model = SVC(kernel='linear', probability=True)
                    model.fit(trainX, trainy)
                    # test model on a random example from the test dataset
                    #selection = choice([i for i in range(testX.shape[0])])
                    for i in range (testX.shape[0]):
                        #print(i)
                        selection=i
                        #print("Selection=",selection)
                        random_face_pixels = testX_faces[selection]
                        random_face_emb = testX[selection]
                        random_face_class = testy[selection]
                        random_face_name = out_encoder.inverse_transform([random_face_class])
                        # prediction for the face
                        samples = expand_dims(random_face_emb, axis=0)
                        yhat_class = model.predict(samples)
                        yhat_prob = model.predict_proba(samples)
                        # get name
                        class_index = yhat_class[0]
                        class_probability = yhat_prob[0,class_index] * 100
                        predict_names = out_encoder.inverse_transform(yhat_class)
                        print('Predicted: %s (%.3f)' % (predict_names[0], class_probability))
                        pred=predict_names[0]
                        #print(pred)
                        #c.execute('SELECT Name FROM students WHERE Reg_No=(?)',(pred,))
                        var=("SELECT Name FROM students WHERE Reg_No=%s")
                        #print(pred,class_probability)
                        #print(pred)
                        var2=(int(pred),)
                        c.execute(var,var2)
                        row=c.fetchone()
                        #print("Predicted=",row)
                        #print('Expected: %s' % random_face_name[0])
                        # plot for fun
                        #pyplot.imshow(random_face_pixels)
                        if(class_probability>50):
                            print(pred)
                            #title = '%s (%.3f)' % (predict_names[0], class_probability)
                            title=row[0]
                            atten.append(pred)
                            count=count+1
                        else:
                            title="Unknown"
                        #pyplot.title(title)
                        #pyplot.show()
                    print("Face recognized= ",count)

    atten=list(dict.fromkeys(atten))
    print("atten=",atten)
    for i in atten:

        #c.execute('SELECT Name FROM students WHERE Reg_No=%s',(int(i),))
        #z=c.fetchone()
        #z=(z[0])
        #print("Attendace of",z,"=",int(i))
        a=0
        i=int(i)
        #print("1")
        c.execute('SELECT Attendance FROM students WHERE Reg_No=%s',(i,))
        a=c.fetchone()

        b=list(a)
        #print("b=",b)
        a=b[0]+1
        #print(a)
        #print("3")
        c.execute('UPDATE students SET Attendance=%s where Reg_No=%s',(a,i))
        tech=yr+'t'
        #print(tech)
        abc=0
        #print("2")
       # print(day)
        #print(yr)
        #print(serial)

        c.execute("SELECT "+day+" from "+yr+" where Serial=%s",(serial,))
        #statement="""SELECT %s from from %s where No=%s""" %(day,yr,serial)
        #c.execute(statement)
        abc=c.fetchone()
        #print(abc[0])
        new=abc[0]
        #new=''.join(abc[0])
        new=new.split('-')
        new=''.join(new[0])
        new=new.strip()
        #print("new=",new)
        c.execute('SELECT '+new+' from '+tech+' where UID=%s',(i,))
        sat=c.fetchone()
        sat=list(sat)
        sat=sat[0]+1
        print("Student ATT=",sat)
        #c.execute('UPDATE be6t SET PM')
        c.execute('UPDATE '+tech+' SET '+new+'=%s where UID=%s',(sat,i) )
        '''
        if day=='Monday':
            print(abc[2])
        elif day=='Tuesday':
            print(abc[3])
        elif day=='Wednesday':
            print(abc[4])
        elif day=='Thursday':
            print(abc[5])
        elif day=='Friday':
            print(abc[6])
        '''
    #print(yr,day,serial)    
    final_list=[]   
    for i in atten:
        if i not in final_list:
            final_list.append(i)
    for i in final_list:
        a=0
        i=int(i)
        c.execute('SELECT Attendance FROM students WHERE Reg_No=%s',(i,))
        a=c.fetchone()
        c.execute('SELECT Name FROM students WHERE Reg_No=%s',(int(i),))
        z=c.fetchone()
        z=(z[0])
        print("Attendace of",z,"=",a[0])
    conn.commit()
    conn.close()
