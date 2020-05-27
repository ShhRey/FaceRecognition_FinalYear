
def train():
    # face detection
    from os import listdir
    from os.path import isdir
    from PIL import Image
    from matplotlib import pyplot
    from numpy import savez_compressed
    from numpy import asarray
    from mtcnn.mtcnn import MTCNN

    # extract a single face from a given photograph
    def extract_face(filename, required_size=(160, 160)):
        # load image from file
        image = Image.open(filename)

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

        for filename in listdir(directory):
            # path
            path = directory + filename
            # get face
            face = extract_face(path)
            # store
            faces.append(face)
        return faces

    # load a dataset that contains subdir 
    def load_dataset(directory):
        X, y = list(), list()
        # enumerate folders, on per class
        for folder in listdir(directory):
            print("folder=",folder)
            fname=folder
            a=fname+".npz"
            new_directory=directory+"/"+fname

            print(new_directory)
            for subdir in listdir(new_directory):
                # path
                print("sub=",subdir)
                path = new_directory + "/" + subdir + '/'
                print("path=",path)
                # skip any files that might be in the dir
                '''if not isdir(path):
                    continue'''
                # load all faces in the subdirectory
                faces = load_faces(path)
                # create labels
                labels = [subdir for _ in range(len(faces))]
                # summarize progress
                print('>loaded %d examples for class: %s' % (len(faces), subdir))
                # store
                #print("f=",faces)
                #print("l=",labels)
                X.extend(faces)
                y.extend(labels)
                #print("X=",X)
                #print("Y=",y)
                #print(X.extend(faces),y.extend(labels))
                savez_compressed(a,X,y)



    # load train dataset
    load_dataset('E:/FaceRec/students/train')
    #print("c,b=",c,b)



