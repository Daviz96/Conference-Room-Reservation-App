"""Conference_Room_App URL Configuration

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

import Conf_App.views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', view.Home.as_view(), name='Home'),
    path('room/new/', view.AddRoom.as_view(), name='Add-Room'),
    path('room/list/', view.RoomList.as_view(), name='Room-List'),
    path('room/remove/<int:room_id>/', view.RemoveRoom.as_view(), name='Remove-Room')

]
