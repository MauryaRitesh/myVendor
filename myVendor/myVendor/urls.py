"""myVendor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from profiles import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^profile/', views.userProfile, name='profile'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^services/', views.services, name='services'),
    url(r'^p/potatoes', views.potatoes, name='potatoes'),
    url(r'^p/cauliflower', views.cl, name='cauliflower'),
    url(r'^p/tomato', views.tomato, name='tomato'),
    url(r'^p/spinach', views.spinach, name='spinach'),
    url(r'^p/capcicum', views.capcicum, name='capcicum'),
    url(r'^p/brinjal', views.brinjal, name='brinjal'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^handlerequest/', views.handlerequest, name="HandleRequest"),
    url(r'^accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
