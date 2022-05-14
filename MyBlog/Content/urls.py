from . import views
from django.urls import path
from Content.views import *
from .views import AddPostView
from .views import LikeViev


urlpatterns = [
    path('',views.index, name='index' ),
    path('f/<int:pk>/',views.category_by_id,name = 'cat'),
    path('one_post/<int:id>/',views.post_by_id,name = 'one_post'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('log_out/', views.logout_view, name='log_out'),
    path('add_posts/',AddPostView.as_view(), name= 'add_post'),
    path('search/', views.search_venues, name='search_venues'),
    path('like/<int:pk>/', views.LikeViev, name='like_post'),
]