from django.urls import path,include
from logreg import views

app_name='logreg'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.register_user,name='signup'),
    
    path('special/',views.special,name='special'),
    path('logout/', views.log_request, name='logout'),
]