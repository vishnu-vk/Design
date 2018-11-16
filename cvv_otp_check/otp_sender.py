from twilio.rest import Client
import math,random
from cvv_otp_check.models import User

def send_message(id):
        digits = "0123456789"
        otp_no= "" 
        for i in range(4):
                otp_no += digits[math.floor(random.random() * 10)] 
        otp_field=User.objects.get(Id=id)
        otp_field.otp=int(otp_no)
        otp_field.save()
        account_sid = 'ACdecaf9a46ea8d70eba428afc4872d57b'
        auth_token = 'eb4e6ad2d6a7a58b59fc27b8ad915058'
        myPhone = '+919744172369'
        TwilioNumber = '+18508468314'
        client = Client(account_sid, auth_token)
        client.messages.create(to=myPhone,from_=TwilioNumber,body=otp_no + u'\U0001f680')
        return