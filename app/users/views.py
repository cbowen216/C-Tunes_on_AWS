from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader

from users.models import User
from .serializers import UserSerializer


# Create your views here.

def index(request):
    print("------------------------- I AM HERE")
    queryset = User.objects.all()
    return render(request, "users/index.html", {'users': queryset})

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/index.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})


class list_all_tutorials(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/tutorial_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'tutorials': queryset})

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        email = request.GET.get('email', None)
        if email is not None:
            users = User.filter(title__icontains=email)

        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        User_data = JSONParser().parse(request)
        User_serializer = UserSerializer(data=User_data)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse(User_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(User_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} User were deleted successfully!'.format(count[0])
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