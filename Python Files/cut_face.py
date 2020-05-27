def crop():    
    # extract and plot each detected face in a photograph
    import cv2
    import os
    from matplotlib import pyplot
    from matplotlib.patches import Rectangle
    from matplotlib.patches import Circle
    from mtcnn.mtcnn import MTCNN
    from os import listdir
    from PIL import Image
    import time
    lii=[]
    # draw each face separately
    def cut_faces(directory):
            j=1

            for classr in listdir(directory):
                    directory='E:/OneDrive/val'
                    #print("class=",classr)
                    directory = directory+'/'+classr
                    #print("dir=",directory)
                    for stu in listdir(directory):
                            #print(stu)
                            path = directory +'/'+stu
                            photos = listdir(path)
                            for image in photos:
                                    #print(image)
                                    abc=image
                                    image = path+'/'+image
                                    data = pyplot.imread(image)
                                    detector = MTCNN(); face_list = detector.detect_faces(data)
                                    # plot each face as a subplot

                                    for i in range(len(face_list)):
                                            # get coordinates
                                            #a='a.jpg'
                                            #os.listdir()
                                            #os.rename(abc,'a.jpg')

                                            year="be"
                                            div="6"
                                            print(abc)
                                            #print("%s" % time.ctime(os.path.getctime("IMG-20191028-WA0007.jpg")))
                                            x=os.path.getctime(abc)
                                            y= time.strftime('%H', time.localtime(x))
                                            y12= time.strftime('%M', time.localtime(x))
                                            print(str(y),y12)
                                            #print(j)
                                            x1, y1, width, height = face_list[i]['box']
                                            x1, y1 = x1-30, y1-30
                                            x2, y2 = x1 + width + 55, y1 + height + 55
                                            im = Image.open(image)
                                            im1 = im.crop((x1, y1, x2, y2))
                                            #im1.save(path+'/'+str(j)+'.jpg')
                                            im1.save(path+'/'+str(j)+'-'+str(year)+'-'+div+'-'+str(y)+'-'+str(y12)+'.jpg')
                                            #im1.save(path+'/'+str(y)+'.jpg')
                                            #print(path)
                                            #os.rename(abc,"a.jpg")


                                            j=j+1
                                    #os.remove(image)



    os.chdir("E:/OneDrive/val/be6/13253")
    '''
    for file in os.listdir():
        na=file
        lii.append(na)
        print(lii)
    '''
    directory='E:/OneDrive/val'
    cut_faces(directory)
