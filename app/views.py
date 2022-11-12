from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            
            if password == confirmpassword:
                user = User.objects.create_user(username,email,password)
                customer = Customer.objects.create(user=user, username=username, email=email, password=password)
                customer.save()

                return redirect('login')
            else:
                messages.info(request, 'password not matching')
    except:
        messages.info(request, 'some details are already taken by other user')
    context = {}
    return render(request, 'register.html', context)

@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'homepage.html', context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def showServices(request):
    if request.method == 'POST':
        location = request.POST.get('place')
        services = Service.objects.all().filter(location=location)
        context = {'services':services}
        return render(request, 'showservices.html',context)


@login_required(login_url='login')
def bookService(request,pk):
    sample_user = request.user
    email = sample_user.email
    customer = Customer.objects.get(email=email)
    service = Service.objects.get(id=pk)
    booking = Booking.objects.create(
        customer_details = customer,
        service_details = service,
        status = 'Pending',
    )
    booking.save()
    return redirect('home')

@login_required(login_url='login')
def showBookings(request):
    sample_user = request.user
    email = sample_user.email
    customer = Customer.objects.get(email=email)
    bookings = customer.booking_set.all()
    context = {'bookings':bookings}
    return render(request, 'bookings.html',context)


@login_required(login_url='login')
def adminAddPlaces(request):
    if request.method == 'POST':
        ## need editing
        service = request.POST.get('place')
        new_service = Service.objects.create(location=place)
        new_service.save()
        redirect('home')
    context = {}
    return render(request, 'adminaddplace.html', context)

@login_required(login_url='login')
def adminShowAllBookings(request):
    bookings = Booking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'adminviewbookings.html', context)

@login_required(login_url='login')
def adminModifyStatus(request,pk,status):
    booking = Booking.objects.get(id=pk)
    if status == '1':
        booking.status = 'Accepted'
    else:
        booking.status = 'Rejected'
    booking.save()
    return redirect('home')
    

