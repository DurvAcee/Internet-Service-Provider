from django.contrib import admin
from hello.models import Contact, User, Payment, Plan, Checkout

# Register your models here.
admin.site.register(Contact)

admin.site.register(User)

admin.site.register(Payment)

admin.site.register(Plan)

admin.site.register(Checkout)