from django.urls import path
from .views import *


urlpatterns = [
    path('', News.as_view(), name='home'),
    path('<int:pk>', Post.as_view(), name='post')
]