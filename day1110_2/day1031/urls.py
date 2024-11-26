"""
URL configuration for day1031 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('books.urls')), # 使用自己应用内的路由,例如 'api/' ，但为方便我们就留空
    # path('', include('snippets.urls')), 
    path('', include('guide.urls')), 
    path('api-auth/', include('rest_framework.urls')), # 有这个，才有 DRF 的登录
]
