from django.shortcuts import render
from guide.throttles import BurstRateThrottle
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

# Create your views here.

class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def simple_html_view(request):
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)


from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TrackViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['order','title','album__album_name'] #外键加入两个下划线
    ordering_fields = '__all__'

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)


from rest_framework.views import APIView

class ExampleView(APIView):
    # throttle_classes = [UserRateThrottle]
    throttle_classes = [BurstRateThrottle]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)