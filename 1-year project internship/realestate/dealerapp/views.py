from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from . import models
from  . import  forms
# from buyerapp import models
from buyerapp.models import BookingRequest,property
from django.urls import reverse

# Create your views here.

def login_1(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None and user.is_staff:
            auth.login(request, user)
            return redirect(dashboard_1)
        else:
            return render(request, 'dealerapp/login.html',
                          {'error': 'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request, 'dealerapp/login.html')

def register_1(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'dealerapp/register.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'),
                                                is_staff = True)
                auth.login(request,user)
                return redirect(login_1)
        else:
                return render(request,'dealerapp/register.html',{'error':'password does not match'})

    else:
        return render(request,'dealerapp/register.html')

def about(request):
    return render(request,'dealerapp/about.html')

def dashboard_1(request):
    property_count = property.objects.filter(user=request.user).count()
    booking_count = BookingRequest.objects.count() 
    return render(request,'dealerapp/index.html', {'property_count': property_count, 'booking_count': booking_count})

def adddetails(request):
    if request.method == "POST":
        detailform = forms.detailsform(request.POST, request.FILES)
        if detailform.is_valid():
            object = detailform.save(commit=False)
            object.user = request.user
            object.save()

            photos = request.FILES.getlist('p_image')
            for image in photos:
                img = models.Image.objects.create(p_image=image,proty=object)
            return redirect(managedetails)
        else:
            print(detailform.errors)
            return HttpResponse("<h1>Error</h1>")
    return render(request, 'dealerapp/property-add_details.html')

def managedetails(request):
    data = models.property.objects.filter(user_id=request.user)
    photos = models.Image.objects.all()
    return render(request, 'dealerapp/property-manage.html', {'P_E': data, 'photos': photos})

def edit_property(request,id):
    a=models.property.objects.get(id=id)
    return render(request,'dealerapp/edit_property.html',{'object':a})

def update_property(request, id):
    a = get_object_or_404(models.property, id=id)

    if request.method == "POST":
        updatesform = forms.updateform(request.POST, request.FILES, instance=a)  # include request.FILES
        if updatesform.is_valid():
            updatesform.save()
            return redirect('manage') 
        else:
            print("Form Errors:", updatesform.errors)
            return HttpResponse("<h1>Error: Invalid Form Data</h1>")
    else:
        return render(request, 'dealerapp/edit_property.html', {'object': a})

def delete_property(request,id):
    models.property.objects.filter(id=id).delete()
    return redirect(managedetails)

def showdetails(request,id):
   d = models.property.objects.get(id=id)
   return render(request, 'dealerapp/show_details.html',{'object':d})

def contact(request):
    return render(request,'dealerapp/pages-contact.html')

def profile(request):
    return render(request,'dealerapp/users-profile.html',)

def booking_requests(request):
    br = BookingRequest.objects.all()  # Or filter by dealer if needed
    return render(request, 'dealerapp/bookingrequest.html', {'br': br})

def property_list(request):
    properties = models.property.objects.all()
    return render(request, 'buyerapp/index.html', {'details_from_dealerapp': properties})

def logout(request):
    auth.logout(request)
    return redirect(reverse('admin_dashboard'))
