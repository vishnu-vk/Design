from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from cvv_otp_check.models import User
import os
from django.contrib import messages
from django.http import HttpResponseRedirect
import numpy as np
import cv2
import time
from twilio.rest import Client
import random
from cvv_otp_check.otp_sender import send_message
@csrf_protect



def index(request):
    if request.method=="POST":
        #form=AtmDetails(request.POST)
        #if form.is_valid():
        #print("here it is")
        number=(request.POST.get('number'))
        number=number.replace(' ','')
        number=int(number)
        name=request.POST.get('name')
        cvc=int(request.POST.get('cvc'))
        mm=int(request.POST.get('mm'))
        yyyy=int(request.POST.get('yyyy'))
        try:
            p = User.objects.get(number=number,cvc=cvc,mm=mm,yyyy=yyyy)
        except User.DoesNotExist:
            #print ("Data Not available")
            #message="This card is not valid"
            #dic={'status':message}
            #return render(request,"cvv_otp_check/atm_details.html",context=dic)
            messages.error(request,'Invalid Card Details')
            #return render(request,'cvv_otp_check/atm_details')
        else:
            request.session['cardno']=number
            request.session['Id'] = User.objects.get(number=number).Id
            print(request.session['Id'])
            send_message(request.session['Id'])
            return HttpResponseRedirect('carddetails/otp/')
    return render(request,"cvv_otp_check/atm_details.html")




def otp_page(request):
    if request.method=="POST":
        if request.POST.get("submit_butt"):
            otp=int(request.POST.get('otp'))
            print(otp)
            print(User.objects.get(Id=request.session['Id']).otp)
            if(otp==User.objects.get(Id=request.session['Id']).otp):
                def assure_path_exists(path):
                    dir = os.path.dirname(path)
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                assure_path_exists("trainer/")
                recognizer.read('trainer/trainer.yml')
                cascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(cascadePath)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cam = cv2.VideoCapture(0)
                timeout = 20
                timeout_start = time.time()
                count=0
                while (time.time() < (timeout_start + timeout)):
                    ret, im =cam.read()
                    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2,5)
                    Id=0
                    for(x,y,w,h) in faces:
                        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
                        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                        print(Id)
                        if(Id==request.session['Id'] and (100-confidence)>55):
                            count=count+1
                            if(count>4):
                                print("2ok")
                                return HttpResponseRedirect('/carddetails/status/')
                                
                        
                messages.error(request,'Something Wrong!...')
                cam.release()
                cv2.destroyAllWindows()
            else:
                print("not correct otp")
                messages.error(request,'OTP is not correct!...')
        elif(request.POST.get("resend_butt")):
            send_message(request.session['Id'])
    return render(request,"cvv_otp_check/index.html")

def status(request):
    return render(request,'cvv_otp_check/status.html')


def generate_code():
    return str(random.randrange(100000, 999999))