from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', views.sumit, name= 'sumit'),
    path('', views.tweet_list, name = "tweet_list" ),
    path('create/', views.tweet_create, name = "tweet_create" ),
    path('<int:tweet_id>/edit/', views.tweet_edit, name = "tweet_edit" ),
    path('<int:tweet_id>/delete/', views.tweet_delete, name = "tweet_delete" ),
    path('register/', views.register, name = "register" ),
    path('logged_out', views.logged_out_view, name='logged_out'),
    path('logout/', auth_views.LogoutView(next_page='logged_out'), name='logout'),

]
