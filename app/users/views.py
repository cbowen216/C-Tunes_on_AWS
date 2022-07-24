from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader

from app.users.models import Users

# Create your views here.
User = get_user_model()

def index(request):
    print("------------------------- I AM HERE")
    queryset = Users.objects.all()
    return render(request, "users/index.html", {'users': queryset})

def register(request):
    next = request.GET.get('next', '/')
    try:
        email = request.POST['email']
        password = request.POST['password']
        auth_user = authenticate(request, email=email, password=password)
        try:
            login(request, auth_user)
            return HttpResponseRedirect(next)
        except:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(next)
    except (KeyError):
        messages.error(request, 'Invalid credentials')
        #return render(request, '/', { 'message': "Invalid email or password. Please try again." })


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        print("----------------- register called")
        print(email)
        print(password)
        print(firstname)
        print(lastname)
        print(email)

        # try:
        #     user = get_object_or_404(User, email=email)
        # except:
        #     pass

        messages.success(request,
                         f'Your account has been created! You can now login!')
        return redirect('login')
    else:
        return render(request, 'users/register.html')