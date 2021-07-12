from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Contact, User, Payment, Plan, Checkout
from django.contrib import messages
from django.http import HttpResponse
from pymongo import MongoClient



def home(request):
    return render(request, 'index2.html')

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact(name=name, email = email, message = message, subject = subject)
        c.save()
    return HttpResponse('Your message has been sent. Thank you!')


def signup(request):
    response = HttpResponse(render(request, 'index2.html')) 
    if request.method == "POST":
        fname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        pwd = request.POST.get('password')
        sign1 = User.objects.filter(email=email)
        if len(sign1)>0:
            response.set_cookie('signup','0')  
            return response        
        sign = User(name=fname, email=email, phone=phone, pwd=pwd)
        sign.save()
        response.set_cookie('signup','1')  
        return response
    # return render(request, 'index2.html')


def login(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        # success = User.objects.filter(email=email,pwd=pwd)

        client = MongoClient()
        db = client['demoProj']
        collection = db['hello_user']
        success1 = collection.find({'email':email,'pwd':pwd})

        # if len(success)!=1:
        if success1.count()!=1:
            response = HttpResponse(render(request, 'index2.html'))
            response.set_cookie('signup','2')  
            return response
    response = HttpResponse(render(request, 'plans3.html'))
    response.set_cookie('signup',success1[0]['email'])  
    return response
        
        # success = User.objects.filter(email=email,pwd=pwd)
     
        # if len(success) > 0:
        #     return render(request, 'plans3.html')
        # else:
        #     return render(request,'index2.html')

def makePayment(request):
    if request.method == "POST":
        owner = request.POST.get('username')
        card_num = request.POST.get('cardNumber')
        exp_month = request.POST.get('month')
        exp_year = request.POST.get('year')
        cvv = request.POST.get('cvv')
        pay = Payment(owner=owner,card_num=card_num,exp_month=exp_month,exp_year=exp_year,cvv=cvv)
        pay.save()
    return render(request, 'index2.html')


def choosePlan(request):
    if request.method == "POST":
        
        accno = request.POST.get('accno')
        regno = request.POST.get('regno')
        ch = Checkout(accno=accno,regno=regno)
        ch.save()

    return render(request, 'payment.html')

def listPlan(request):
    
    objs=Plan.objects.all()
    context= {'objs':objs}

    return render(request, 'listplans.html',context)

def checkout(request):
    return render(request, 'checkout.html')

def bill(request):
    if request.method == "POST":
        owner = request.POST.get('username')
        card_num = request.POST.get('cardNumber')
        exp_month = request.POST.get('month')
        exp_year = request.POST.get('year')
        cvv = request.POST.get('cvv')
        email  = request.COOKIES['signup']
        pid=request.COOKIES['plan']
        accno=request.COOKIES['acc']
        mob=request.COOKIES['reg']

        pay = Payment(owner=owner,card_num=card_num,exp_month=exp_month,exp_year=exp_year,cvv=cvv,email=email,planid=pid,accno=accno,mob=mob)
        pay.save()
        objs=Payment.objects.all().last()
        dic1={'name':objs.owner,
        'email':objs.email,
        'mob':objs.mob,
        'accno':objs.accno,}
        
        objs1=Plan.objects.filter(id=objs.planid)[0]
        dic1['price']=objs1.price
        dic1['speed']=objs1.speed
        dic1['validity']=objs1.validity
    return render(request, 'bill.html',dic1)
    # return render(request, 'bill.html')

def returnhome(request):
    return render(request, 'plans3.html')

def pay(request):
    if request.method == "POST":
        accno = request.POST.get('acc')
        mob = request.POST.get('reg')
    pid=request.COOKIES['plan']
    sign1 = Plan.objects.filter(id=pid)
    context={
        'price':sign1[0].price
    }
    response = HttpResponse(render(request, 'payment.html',context))
    response.set_cookie('acc',accno)  
    response.set_cookie('reg',mob)  
    return response