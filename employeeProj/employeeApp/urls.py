
# importing info from views and the path function

from django.urls import path
from . import views


# defining endpoints

urlpatterns = [
    path('', views.index, name='index'),
    path('appInfo/', views.index, name='appInfo')
]