from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),
    path('logout_views', views.logout_view, name='logout'),
    path("register", views.register, name="register"),



    path('schedule', views.schedule, name='schedule'),
    path('certificateStudy', views.certificateStudy, name='certificateStudy'),
    path('certificateStipend', views.certificateStipend, name='certificateStipend'),



    path('<int:pk_page>', views.adpage, name='adpage'),
    path('createad', views.createad, name='createad'),
] 
 