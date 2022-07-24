from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', user_views.index.as_view(), name='home'),
     path('api/users/', user_views.user_list)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


'''
    path('register/', user_views.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='user/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='user/logout.html'),
         name='logout'),
'''