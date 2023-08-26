"""media_processing_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
import ptvsd

# Check if in DEBUG mode before starting ptvsd to ensure it doesn't run in production
if settings.DEBUG:
    print('attaching ptvsd')
    ptvsd.enable_attach(address=('0.0.0.0', 5678))
    ptvsd.wait_for_attach()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transcript_app.urls')),
]
