from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artists.models import Artist
from artists.serializers import ArtistSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "artists/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Artist.objects.all()
    return render(request, "artists/index.html", {'artists': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artists/index.html'

    def get(self, request):
        queryset = Artist.objects.all()
        return Response({'artists': queryset})


class list_all_artists(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artists/artist_list.html'

    def get(self, request):
        queryset = Artist.objects.all()
        return Response({'artists': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def Artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            artists = artists.filter(title__icontains=name)

        artists_serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(artists_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Artist_data = JSONParser().parse(request)
        Artist_serializer = ArtistSerializer(data=Artist_data)
        if Artist_serializer.is_valid():
            Artist_serializer.save()
            return JsonResponse(Artist_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(Artist_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Artist.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Artist were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def Artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return JsonResponse({'message': 'The Artist does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Artist_serializer = ArtistSerializer(artist)
        return JsonResponse(Artist_serializer.data)

    elif request.method == 'PUT':
        Artist_data = JSONParser().parse(request)
        Artist_serializer = ArtistSerializer(artist, data=Artist_data)
        if Artist_serializer.is_valid():
            Artist_serializer.save()
            return JsonResponse(Artist_serializer.data)
        return JsonResponse(Artist_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Artist.delete()
        return JsonResponse({'message': 'Artist was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
