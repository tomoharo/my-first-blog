# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]


if __name__ == "__main__":
    pass