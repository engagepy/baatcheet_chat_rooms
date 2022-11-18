from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

 # OTP related imports only below:

from django.conf import settings
from django.core.mail import send_mail
import math, random
from threading import Thread
import datetime

# def generateOTP() :
#      digits = "0123456789"
#      OTP = ""
#      for i in range(4) :
#          OTP += digits[math.floor(random.random() * 10)]
#      return OTP

# def send_otp(request):
#      email=request.POST.get("email")
#      print(email)
#      o=generateOTP()
#      send_mail(
#         subject='OTP',
#         message=o,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[email],
#         fail_silently=False, 
#         )
#      return HttpResponse(o)

def sendwelcome(email):
    #Calculating Time, and limiting decimals
    x = datetime.datetime.now()
    s = x.strftime('%Y-%m-%d %H:%M:%S.%f')
    s = s[:-6]
    y = f'Thanks for loggin into `BaatCheet` at {s} Respond to this email with your feedback or any incident you need to report, cheers.'
    #using the send_mail import below
    send_mail(
        subject='BaatCheet - Welcomes You',
        message=y,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
        )

# OTP related functions end above

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'No Email Found in Database')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            Thread(target=sendwelcome, args=(email,)).start()
            return redirect('home')
        else:
            messages.error(request, 'Credentials are incorrect, please retry!')

    loginPage_data = {'page':page}
    return render(request, 'base/login_register.html', loginPage_data )

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'Password Note: 8 characters minimum, 1 Upper, 1 lower & 1 numeric madatory ')
    return render(request, 'base/login_register.html', {'form': form})

@login_required(login_url="accounts/login")
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topic = Topic.objects.all()[0:6]
    room_count = rooms.count()
    topicx = Topic.objects.all().count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    home_data = {'rooms': rooms, 'topics': topic, 'room_count': room_count,'topicx':topicx, 'room_messages':room_messages }
    return render(request, 'base/home.html', home_data )

@login_required(login_url="accounts/login")
def room(request, id):
    room = Room.objects.get(id=id)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
        )
        room.participants.add(request.user)
        return redirect ('room', id=room.id)

    room_data = {'room': room, 'room_messages': room_messages, 'participants':participants}
    return render(request, 'base/room.html', room_data)

@login_required(login_url="accounts/login")
def userProfile(request, id):
    user = User.objects.get(id=id)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    topicx = Topic.objects.all().count()
    profile_data = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics':topics,'topicx':topicx}
    return render(request, 'base/profile.html', profile_data)

@login_required(login_url="accounts/login")    
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        # Get_Or_Create Object Below

        

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')


        #Another Method Form 

        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        #     print(request.POST)
        #     return redirect('home')

    create_data = {'form': form , 'topics': topics}
    
    return render(request, 'base/room_form.html', create_data)

@login_required(login_url="accounts/login") 
def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('Not Allowed!')

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    update_data = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', update_data)

@login_required(login_url="accounts/login") 
def deleteRoom(request, id):
    room = Room.objects.get(id=id)

    if request.user != room.host:
        return HttpResponse('Not Allowed!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})

@login_required(login_url="accounts/login") 
def deleteMessage(request, id):
    message = Message.objects.get(id=id)

    if request.user != message.user:
        return HttpResponse('Not Allowed!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url="accounts/login")
def updateUser(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect ('userprofile', id=user.id)


    return render(request,'base/updateuser.html' , {'form': form})
@login_required(login_url="accounts/login")
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})
@login_required(login_url="accounts/register")
def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})


