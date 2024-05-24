# App's own url file
from django.urls import path 
# from .views import first,table,nav,reg,auth,feed,login
from .views import *

 
urlpatterns = [
    # path ('whatever' , function of views file , name = 'whatever you like')
    path('first/', first , name = 'first'),
    path('table/', table , name='tb'),
    path('nav/', nav, name='nav'),
    path('auth/', auth, name='auth'),
    path('reg/' , reg, name='reg'),
    path('feed/' , feed, name='feed'),
    path('login/' , login, name='login'),
    path('logout/' , logout, name='logout'),
    path('profile/' , profile,name='profile'),
    path('edit_profile/' , EditProfile , name="EditProfile"),
    path('changePass/' , changePass , name="changePass"),
    path('Home/' , Home ,name='Home') , 
    path('seat/<int:id>' , seat ,name='seat') , 
    path('cart/' , cart ,name='cart') , 
    path('remove/<int:agency> <int:id>' , remove ,name='remove') , 
    path('removeall/' , removeall ,name='removeall') , 
    path('categ/' , categ ,name='categ') , 
    path('agen_reg/' , agen_register, name='agen_reg'),
    path('add_bus/' , add_bus, name='add_bus'),
    path('agen_login/' ,agen_login , name='agen_login'),
    path('about_us/', about_us, name='about_us'),
    path('agen_added/' ,agen_added , name='agen_added'),
    path('delete_agen/<int:id>' ,delete_agen , name='delete_agen'),
    path('update_agen/<int:id>' ,update_agen , name='update_agen'),
    path('checkout/' ,checkout , name='checkout'),
    path('razorpay/' ,razorpayView , name='razorpay'),
    path('paymenthandler/' ,paymenthandler , name='paymenthandler') , 
    path('my_order/' ,my_order , name='my_order') , 
    ]