from django.urls import path
from . import views

app_name = "movie" #in case there is ambiguity with other module in function naming

urlpatterns = [
    path('movie_id/<int:movie_id>/movie_name/<str:movie_name>',views.movie_id_search,name="movie_search")
]