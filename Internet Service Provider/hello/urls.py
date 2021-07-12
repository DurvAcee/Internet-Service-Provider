from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('index', views.index, name = "index"),
    path('home', views.signup, name = "signup"),
    path('login', views.login, name = "login"),
    path('plan',views.choosePlan, name = "plan"),
    path('payment',views.makePayment, name = "payment"),
    path('listplan',views.listPlan),
    path('checkout',views.checkout, name = "checkout"),
    path('bill',views.bill, name = "bill"),
    path('returnhome',views.returnhome, name = "returnhome"),
    path('plan1',views.pay)
    
]
