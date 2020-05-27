def test():
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
        train='E:/flask/'+classroom+'.npz'
        
        data = load(train)
        #print(train)
        #print("data=",data['arr_0'])
        #print("data2=",data['arr_1'])
        
        test='E:/flask/'+classroom+'-test.npz'
        #print(test)
        data1=load(test)
        #print("data3=",data1['arr_0'])
        #print("data4=",data1['arr_1'])


        trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data1['arr_0'], data1['arr_1']
        print('Loaded: ', trainX.shape, trainy.shape, testX.shape, testy.shape)
        # load the facenet model

        model = load_model('E:/flask/facenet_keras.h5')
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
        savez_compressed('E:/flask/'+classroom+'-embedding.npz', newTrainX, trainy, newTestX, testy)
        #print(newTrainX, trainy, newTestX, testy)
        embed='E:/flask/'+classroom+'-embedding.npz'
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
                print("1")    
                # load all faces in the subdirectory
                faces = load_faces(path)
                # create labels
                labels = [subdir for _ in range(len(faces))]
                # summarize progress
                print('>loaded %d examples for class: %s' % (len(faces), subdir))
                # store
                X.extend(faces)
                y.extend(labels)
                print("classroom=",classroom)
                a=classroom+'-test.npz'
                savez_compressed("E:/flask/"+a,X,y)
                print("inside loaddata")
                directory='E:/OneDrive/val'
                print("classroom2=",classroom)
                embed(classroom)
    # load train dataset
    #div=input("Enter your division")
    #year=input("Enter your year")
    #div1=div
    #year1=year
    # load test dataset

    p='E:/OneDrive/val'
    print(p)
    load_dataset(str(p))
    print("data trained")
    # save arrays to one file in compressed format
    #print(testX.shape,testy.shape)







































