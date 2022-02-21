from . import views
from django.urls import path
from Content.views import *


urlpatterns = [
    path('',views.index, name='index' ),
    path('f/<int:id>/',views.category_by_id,name = 'cat'),
    path('one_post/<int:id>/',views.post_by_id,name = 'one_post'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('log_out/', views.logout_view, name='log_out'),
]