from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # 重写这个函数，就可以改变新增行为，面向切面编程
    # 具体细节在继承关系里，需要看源码
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from snippets.permissions import IsOwnerOrReadOnly
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


from django.contrib.auth.models import User
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer] # 配置渲染器

    def get(self, request, *args, **kwargs):
        snippet = self.get_object() # 在详情页中拿到了某个 snippet 对象
        return Response(snippet.highlighted)



from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })