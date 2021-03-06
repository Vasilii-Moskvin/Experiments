"""notetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from mainapp.views import *
from userManagementApp.views import *
from workWithNote.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    url(r'^user/registration/$', registration),
    url(r'^user/create_note/$', create_note),
    url(r'^user/save_note/$', save_note),
    url(r'^user/note/([\w-]+)/$', open_note, name='public_note_view'),
    url(r'^user/change_note/([\w-]+)/$', change_note, name='public_note_change'),
    url(r'^user/delete_note/([\w-]+)/$', delete_note, name='public_note_delete')
]
