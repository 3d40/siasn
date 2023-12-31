"""apisiasn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'intaian'
urlpatterns = [
    path('token/pertama', views.ViewAuth, name='tokenpertama'),
    path('token/kedua', views.ViewAuthorization, name='tokenkedua'),
    path('data/<str:nip>', views.get_data, name='datautama'),
    path('rwgolongan/<str:nip>', views.get_rwgolongan, name='rwgolongan'),
    path('pasangan/<str:nip>', views.get_pasangan, name='pasangan'),
    path('rwpendidikan/<str:nip>', views.get_pendidikan, name='rwpendidikan'),
    # path('coba/<str:nip>', views.coba, name='coba')
]
