from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from .serializers import BookInfoSerializer
# Create your views here.
class BookInfoAPIView(ModelViewSet):
    # 当前视图类所有方法使用得数据结果集是谁?(从哪一个模型里查数据)
    queryset = BookInfo.objects.all()
    # 当前视图类使用序列化器类是谁
    serializer_class = BookInfoSerializer
    # 上面两个实际上是面向切面编程