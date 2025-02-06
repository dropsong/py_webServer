from django.contrib import admin
from django.urls import path, include, re_path
from guide.views import AlbumViewSet, FileUploadView, TrackViewSet, UserViewSet, simple_html_view, CommentViewSet, EventViewSet
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'comment', CommentViewSet)
router.register(r'event', EventViewSet)
router.register(r'users', UserViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    path('upload/<str:filename>/', FileUploadView.as_view()),
    path('simple_html_view/', simple_html_view),
    path('example_view/', example_view),
    path('example_view1/', ExampleView.as_view()),
]

urlpatterns += router.urls