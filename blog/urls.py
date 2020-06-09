from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('blog/', blog, name='blog'),
    path('search/', search, name='search'),
    path('post/<id>/', post, name='post'),

]
