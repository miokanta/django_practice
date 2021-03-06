"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('hoge/',include("hoge.urls")),
    path('fuga/<foo>',views.fuga),
    path("search",views.search),
    path("form",views.form),
    path("upload",views.upload),
    path("login",views.login),
    path("post",views.post),
    path("search",views.search),
    path("delete",views.delete),
    path("change_title",views.change_title),
    path("page_form",views.page_form), 
    path("page_post",views.page_post),
    path("page_list",views.page_list),
    # path("{"id"}/pages",views.page_post),
    path("admin/",admin.site.urls)
]
