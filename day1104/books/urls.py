from rest_framework.routers import DefaultRouter
# 之前导入的是函数视图，现在改为类视图，参见：
# https://github.com/dropsong/py_webServer/blob/master/day1010/booktest/urls.py
from .views import BookInfoAPIView
# from books import views

urlpatterns = []

# 创建路由对象
routers = DefaultRouter()

# 通过路由对象对视图类进行路由生成
# 通过 restful 设计，注册类视图
routers.register("books",BookInfoAPIView) 

urlpatterns+=routers.urls
