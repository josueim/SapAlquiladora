"""SapAlquiladora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppAlquiladora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('inicio/', views.signin, name='signin'),
    path('registro/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('mobiliario/', views.mobiliario, name='mobiliario'),
    path('mobiliario-p/', views.mobiliario_p, name='mobiliario_p'),
    path('personal/', views.personal, name='personal'),
    path('personal-p/', views.personal_p, name='personal_p'),
    path('platillos/', views.platillos, name='platillos'),
    path('platillos-p/', views.platillos_p, name='platillos_p'),
    path('presupuesto/', views.presupuesto, name='presupuesto'),
    path('vista-platillos/', views.vista_platillos, name='vista_platillos'),
]
