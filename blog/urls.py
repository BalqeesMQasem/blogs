from django.urls import path
from .views import *


urlpatterns = [
    path('get-csrf-token/', csrf_token_view, name='get_csrf_token'),
    path('current_user/', current_user),
    path('index_blogs/', index_blogs),
    path('<int:blog_id>/', show_blog, name='show_blog'),
    path('create/', create_blog, name='create_blog'),
    path('update/<int:pk>/',update_blog, name= "update_blog" )
]
