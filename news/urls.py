from django.urls import path
from .views import *


urlpatterns = [
    path('', News.as_view(), name='home'),
    path('<int:pk>', PostView.as_view(), name='post'),
    path('search/', SearchPost.as_view(), name='search'),
    path('add/', AddPost.as_view(), name='add'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]