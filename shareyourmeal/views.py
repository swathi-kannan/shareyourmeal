from django.http import HttpResponse 
from django.shortcuts import render , redirect
from shareyourmeal.models import Userreg 
from shareyourmeal.models import Pay
from shareyourmeal.models import Addpost
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def Payment(request):
    if request.method == 'POST':
        reason = request.POST.get('reason') 
        rupee = int(request.POST.get('rupee')) * 100
        client=razorpay.Client(auth=("rzp_test_WbxRH8SOiX13US" , "mox6ObLe0mXcJ9QRCBdgzyOJ"))
        payment = client.order.create({'amount':rupee, 'currency':'INR', 'payment_capture' : '1'})
        pay= Pay(reason= reason , rupee= rupee, payment_id = payment['id'])
        return render(request, "donate.html" , {'payment' : payment})

    return render(request,'donate.html')
@csrf_exempt
def success(request):
    if request.method =="POST":
        a = request.POST
        print(a)
    return render(request, "success.html")

def aboutus(request):
    return render(request,'aboutus.html')
def Post(request):
    if request.method == 'POST':
        if request.POST.get('reason') and request.POST.get('count') and request.POST.get('phoneno') and request.POST.get('address') and request.POST.get('caption'):
            saverecord=Addpost()
            saverecord.reason=request.POST.get('reason')
            saverecord.count=request.POST.get('count')
            saverecord.phoneno=request.POST.get('phoneno')
            saverecord.address=request.POST.get('address')
            saverecord.caption=request.POST.get('caption')
            saverecord.save()
            messages.success(request,'Posted successfully')
            return render(request,'socio.html')
    else:
        return render(request,'socio.html')
def profile(request):
    return render(request,'profile.html')
def Userregistration(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('phoneno') and request.POST.get('address') and request.POST.get('password') and request.POST.get('type'):
            saverecord=Userreg()
            saverecord.username=request.POST.get('username')
            saverecord.email=request.POST.get('email')
            saverecord.phoneno=request.POST.get('phoneno')
            saverecord.address=request.POST.get('address')
            saverecord.password=request.POST.get('password')
            saverecord.type=request.POST.get('type')
            saverecord.save()
            messages.success(request,'Registered successfully')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        try:
            Userdetails=Userreg.objects.get(username=request.POST['username'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['username']=Userdetails.username
            return redirect('socio')
        except Userreg.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid')
    return render(request,'login.html')
def logout(request):
    try:
        del request.session['username']
    except:
        return render(request, 'donate.html')
    return render(request, 'donate.html')
    
