from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader

from users.models import Users
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
User = get_user_model()

def index(request):
    print("------------------------- I AM HERE")
    queryset = User.objects.all()
    return render(request, "users/index.html", {'users': queryset})

@api_view(['GET', 'POST', 'DELETE'])
def User_list(request):
    if request.method == 'GET':
        artists = User.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            artists = artists.filter(title__icontains=title)

        artists_serializer = UserSerializer(artists, many=True)
        return JsonResponse(artists_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Artist_data = JSONParser().parse(request)
        Artist_serializer = UserSerializer(data=Artist_data)
        if Artist_serializer.is_valid():
            Artist_serializer.save()
            return JsonResponse(User_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(User_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Artist were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

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