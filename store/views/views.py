
from django.conf import settings
from twilio.rest import Client
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random


class MessageHandler:
    phone_number=None
    otp=None
    def __init__(self,phone_number,otp) -> None:
        self.phone_number=phone_number
        self.otp=otp
    def send_otp_via_message(self):     
        client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(body=f'your otp is:{self.otp}',from_=f'{settings.TWILIO_PHONE_NUMBER}',to=f'{settings.COUNTRY_CODE}{self.phone_number}')
    def send_otp_via_whatsapp(self):     
        client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(body=f'your otp is:{self.otp}',from_=f'{settings.TWILIO_WHATSAPP_NUMBER}',to=f'whatsapp:{settings.COUNTRY_CODE}{self.phone_number}')
    def register(request):
        otp=random.randint(1000,9999)
        messagehandler=MessageHandler('7981676619',otp).send_otp_via_message()
        return render(request , 'enter_otp.html',{'otp' : otp})

        
    def verify_otp(request):
        user_otp = request.POST.get("user_otp")
        twilio_otp = request.POST.get("twilio_otp")
        if(user_otp==twilio_otp):
            return redirect('homepage')
        else:
            return render (request, 'login.html', {'error': 'INVALID OTP, PLEASE LOGIN AGAIN!!'})
    def enter_otp(request):
        return render('enter_otp.html')

            
    




