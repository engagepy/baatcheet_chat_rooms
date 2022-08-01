from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('/', views.home, name="home"),
    path('room/<str:id>/', views.room, name="room"),
    path('profile/<str:id>', views.userProfile, name="userprofile"),
    path('createroom/', views.createRoom, name="createroom"),
    path('updateroom/<str:id>/', views.updateRoom, name="updateroom"),
    path('deleteroom/<str:id>/', views.deleteRoom, name="deleteroom"),
    path('deletemessage/<str:id>/', views.deleteMessage, name="deletemessage"),

    path('updateuser/', views.updateUser, name="updateuser"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    

]

