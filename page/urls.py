from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'page'
urlpatterns =[
    path('',views.index,name='index'),
    path('(?P<album_id>[0-9]+/)', views.details,name='details'),
    path('add_album',views.add_album,name='add_album'),
    path('(?P<album_id>[0-9]+)/add_song', views.add_song, name='add_song'),
    path('(?P<album_id>[0-9]+)/delete-album', views.delete_album, name='delete-album'),
    path('signup',views.signup, name='signup'),
    #path('login', auth_views.LoginView.as_view(), name='login'),
    #path('logout',auth_views.LogoutView.as_view(), name='logout'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('(?P<album_id>[0-9]+)/update',views.update_album, name='update'),
    path('(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/',views.delete_song, name='delete_song'),
    path('(?P<album_id>[0-9]+)/update_song/(?P<song_id>[0-9]+)/', views.update_song, name='update_song'),

]