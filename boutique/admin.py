from django.contrib import admin
from.models import *


# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display = ("name","email","phone","address","sex","age","city","zip_code","created_date","save_by")




class AdminInvoice(admin.ModelAdmin):
    list_display = ("customer","save_by","invoice_date_time","total","paid","invoice_type","comments")
  

class AdminArticle(admin.ModelAdmin):
     list_display = (" invoice","name","quantity","unit_price","total")


admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)
   