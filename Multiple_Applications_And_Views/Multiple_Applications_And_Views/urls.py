"""Multiple_Applications_And_Views URL Configuration

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
from APP1 import views as A1views
from APP2 import views as A2views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('A1V1/',A1views.V1),
    path('A1V2/',A1views.V2),
    path('A2V1/',A2views.V1),
    path('A2V2/',A2views.V2),
]
