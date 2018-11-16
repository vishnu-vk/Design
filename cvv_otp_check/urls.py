from django.conf.urls import url
from cvv_otp_check import views

app_name = 'cvv_otp_check'

urlpatterns = [

url(r'^otp/',views.otp_page,name='otp'),
url(r'^status/',views.status,name='status')

]
