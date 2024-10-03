from django.shortcuts import render,HttpResponse
# Create your views here.


def movie_id_search(request,movie_id,movie_name):

    return HttpResponse(f"The id you searched is: {movie_id},name is {movie_name}.")
















