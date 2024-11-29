from django.shortcuts import render
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

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

