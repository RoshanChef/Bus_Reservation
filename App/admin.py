from django.contrib import admin
# from .models import register ,bus ,  author , feedback , ticket ,state
from .models import *

from import_export.admin import ImportExportModelAdmin
from import_export import resources


# class register_(admin.ModelAdmin):
class register_(ImportExportModelAdmin):
    list_display =['id','name', 'number', 'email', 'address','password']
    search_fields = ['name']
    list_filter = ['name']

class author_(admin.ModelAdmin):
    list_display = ['id','name', 'post']

class feedback_(admin.ModelAdmin):
    list_display = ['id' , 'name', 'email', 'message']
    list_filter = ['email']

class state_(ImportExportModelAdmin):
    list_display = ['id' , 'state'  , 'seats'] 
    search_fields = ['state']

class ticket_(ImportExportModelAdmin):
    list_display = ['id' , 'email' ,'orderid' ,'source' , 'destination','stateid','agencyid' , 'numTickets' , 'price'] 
    search_fields = ['email','source']
    list_filter = ['email' , 'destination' , 'source']

class bus_(ImportExportModelAdmin):
    list_display = ['id' ,'agency', 'state' , "agencyid" , 'stateid','busid' , 'price','seats'] 
    search_fields = ['stateid']

class agen_reg_(ImportExportModelAdmin):
    list_display =['id','agen_name','name', 'number', 'email', 'address','password']
    search_fields = ['agen_name']
    list_filter = ['agen_name']

class order_(ImportExportModelAdmin):
    list_display =['id','orderid','city', 'state', 'pincode','transactionid','datetime']
    search_fields = ['orderid']
    list_filter = ['state']



# Register your models here.

admin.site.register(register , register_)
admin.site.register(author , author_)
admin.site.register(feedback , feedback_)
admin.site.register(state , state_)
admin.site.register(bus , bus_)
admin.site.register(ticket , ticket_)
admin.site.register(agen_reg,agen_reg_)
admin.site.register(order,order_)