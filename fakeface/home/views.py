from statistics import mode
from django.shortcuts import render,HttpResponse, resolve_url
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import cv2
from django.core.files.storage import FileSystemStorage
from matplotlib import pyplot as plt
import os
model = load_model( "static/fake_face_detection.h5")
# Create your views here.
def index(request):
    return HttpResponse('Success')
def contact(request):
    return render (request,'contact.html')
def about(request):
        
    return render (request,'about.html')
# 

model = load_model( "static/fake_face_detection.h5")
predictions=''
filePathName=''

  
def face(request):
    global filePathName
    if request.method=="POST":
        print (request)
    # print (request.POST.dict())
        fileObj= request.FILES.get('myfile', None)
        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name,fileObj)
        filePathName=fs.url(filePathName)
        # print("dddddddddddddddddddddddddddddddddddddddddddd",filePathName)
        # model = load_model( "static/fake_face_detection.h5")

        # img = cv2.imread(filePathName)
        # # print("fddddddddddddddddddddddd".img)
        # res = cv2.resize(img, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
        # res = res.reshape(1,224,224,3)
        # predictions = model.predict(res)
        print(predictions)
            
        
    return render (request,'fc.html',{'filePathName':filePathName})#,{'predictions':predictions})

    # global predictions
    # global model
    # if request.method == 'POST':

     

    #    ff = request.FILES['myfile']
    #    print(ff) static=('static/my/check.jpg')
       
      
    #    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",ff)
    #   #   static=('static/my/check.jpg')
    #    img= cv2.imread(r'ff')
    # #img = cv2.imread(static)

    # #res = cv2.resize(img, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
    #    frame = cv2.resize(img,dsize=(224,224),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    #    res = frame.reshape(1,224,224,3)
    #    predictions = model.predict(res)
    #    print(predictions)
       #




def fake(request):

   # model = load_model('fake_face_detection.h5')
    #model = load_model( "static/fake_face_detection.h5")
    print(model.summary())
    img = cv2.imread('./static/my/beauty.jpg')
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename()
    print( "ffffffffffffffffffffffffffffffff", filename)
    #f#ilename="/media/20161124_124202.jpg"
    
    img = cv2.imread(  filename)
   
   
    res = cv2.resize(img, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
    res = res.reshape(1,224,224,3)
    predictions = model.predict(res)
    print(predictions)
    
        # print(('real={:.0%}, fake={:.0%}'.format(predictions[0][1],predictions[0][0])))
   # rest=('real={:.0%}, fake={:.0%}'.format(predictions[0][1],predictions[0][0]))
    rest=('{:.0%}'.format(predictions[0][1]))
    rests=(' {:.0%}'.format(predictions[0][0]))
    #print(('real={:.0%}, fake={:.0%}'.format(predictions[0][1],predictions[0][0])))
   
    return render (request,'home.html',{'predictions':predictions,'rest':rest,'rests':rests,'filename':filename})
  
    