from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "users/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = User.objects.all()
    return render(request, "users/index.html", {'users': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/index.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})


class list_all_users(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/user_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def User_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        name = request.GET.get('email', None)
        if name is not None:
            users = users.filter(title__icontains=name)

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
                '{} Users were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def User_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except user.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        User_serializer = UserSerializer(user)
        return JsonResponse(User_serializer.data)

    elif request.method == 'PUT':
        User_data = JSONParser().parse(request)
        User_serializer = UserSerializer(User, data=User_data)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse(User_serializer.data)
        return JsonResponse(User_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        User.delete()
        return JsonResponse({'message': 'User was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
