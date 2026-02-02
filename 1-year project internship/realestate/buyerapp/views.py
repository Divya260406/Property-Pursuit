from django.shortcuts import render , HttpResponse,redirect
from dealerapp import models
from buyerapp import forms
from django.contrib import auth
from django.contrib.auth.models import User
from buyerapp.models import BookingRequest
from dealerapp.models import property,Image

# Create your views here.
def login_0(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None and not user.is_staff and not user.is_superuser:
            auth.login(request, user)
            return redirect(index)
        else:
            return render(request, 'buyerapp/login.html',{'error': 'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request, 'buyerapp/login.html')

def register_0(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'buyerapp/register.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'))

                auth.login(request,user)
                return redirect(login_0)
        else:
                return render(request,'buyerapp/register.html',{'error':'password does not match'})

    else:
        return render(request,'buyerapp/register.html')

def index(request):
    data = models.property.objects.all()
    photos = models.Image.objects.all()
    context = {'data': data,'photos':photos}
    return render(request,'buyerapp/index.html',context=context)

def property_details(request,id):
    pd = models.property.objects.get(id=id)
    photos = models.Image.objects.all()
    return render(request, 'buyerapp/property-details.html',{'o':pd, 'photos':photos})

def sendrequest(request,id):
    pd = models.property.objects.get(id=id)
    print(pd)
    form =  BookingRequest()
    if request.method == "POST":

        print("helooooooooooooooo")
        form.user=request.user
        print(form.user)
        form.prop=pd
        print(form.prop)
        form.save()
        print("objects",form)
        return redirect(index)
        # else:
        #     print(form.errors)
    return render(request,'buyerapp/property-details.html')

def properties(request):
    props = property.objects.all().prefetch_related('image_set')  # prefetch related images
    return render(request, 'buyerapp/properties.html', {'properties': props})


def buy(request):
    return render(request,'buyerapp/buy.html')

def view_list(request):
    return render(request,'buyerapp/view-list.html')


def about(request):
    return render(request,'buyerapp/about.html')

def buyerapp_contact(request):
    return render(request,'buyerapp/contact.html')

def another_view(request):
     data= models.property.objects.all()
     context={'data':data}
     return render(request,'buyerapp/index.html',context=context)


def buyer_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        user = request.user
        user.username = username
        user.email = email
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('buyer-profile')  # Update name if needed

    return render(request, 'buyerapp/profile.html')




