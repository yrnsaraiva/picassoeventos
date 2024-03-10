from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Event, PastEvents, FutureEvents
from django.contrib.auth.decorators import login_required

# Create your views here.

# events = [
#     {'id': 1, 'name': 'event 1', 'description': 'description 1'},
#     {'id': 2, 'name': 'event 2', 'description': 'description 2'},
#     {'id': 3, 'name': 'event 3', 'description': 'description3'}
# ]


def index(request):
    events = Event.objects.all()
    past_events = PastEvents.objects.all()
    future_events = FutureEvents.objects.all()

    context = {'events': events, 'past_events': past_events, 'future_events': future_events}
    return render(request, 'base/index.html', context)


def events(request):
    events = Event.objects.all()
    future_events = FutureEvents.objects.all()

    context = {'events': events, 'future_events': future_events}
    return render(request, 'base/events.html', context)


def eventDetails(request, pk):
    event = Event.objects.get(id=pk)

    context = {'event': event, 'pk': pk}
    return render(request, 'base/event-details.html', context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context = {'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()

    return render(request, 'base/register.html')


@login_required(login_url='login')
def updateUser(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')

        User.objects.upadate_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()

    return render(request, 'base/register.html')


def about(request):
    return render(request, 'base/about.html')


def gallery(request):
    return render(request, 'base/gallery.html')


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}

    return render(request, 'base/user.html', context)


def contactPage(request):
    return render(request, 'base/contact.html')