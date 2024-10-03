"""
URL configuration for tree_django_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include,reverse
from django.shortcuts import HttpResponse
from book import views

def index(request):
    print(reverse("index"))
    print(reverse("book_query_string_2",kwargs={"book_id":5,"book_name":"tree_book"}))
    print(reverse("movie:movie_search",kwargs={"movie_id":5,"movie_name":"tree_movie"}))
    return HttpResponse("树的姜戈！")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"), #'' means 127.0.0.1:8000
    path("book",views.book_id_search,name="book_query_string"), #如果使用reverse 只能手动拼接
    path("book/<int:book_id>/name/<str:book_name>",views.book_id_search_2,name="book_query_string_2"),
    path("book/<path:book_path>",views.book_path,name="book_path_name"),

    path("movie/", include("movie.urls"))
]
