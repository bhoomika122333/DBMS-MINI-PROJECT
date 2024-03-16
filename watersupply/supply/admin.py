from django.contrib import admin
from .models import Bottle,Order,User,Company,OrderAddress,UserDetails

# Register your models here.
admin.site.register(Bottle)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(OrderAddress)
admin.site.register(UserDetails)
