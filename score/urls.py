# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.add,name='add'),
    path('addpoint',views.addpoint,name='addpoint'),
    path('video',views.video,name='video'),
    path('analys/<int:num>', views.analys, name='analys'),
    path('edit/<int:num>',views.edit,name='edit'),
    path('find', views.find, name='find'),
    path('person/<int:num>', views.person, name='person'),
]