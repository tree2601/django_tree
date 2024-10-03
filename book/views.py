from django.shortcuts import render,HttpResponse

# Create your views here.

# 127.0.0.1:8000/book?id=1&name=temp
def book_id_search(request):
    book_id = request.GET.get("id")  #GET is just a dict. 
    book_name = request.GET.get("name")
    return HttpResponse(f"The id you searched is: {book_id},name is {book_name}.")


def book_id_search_2(request,book_id,book_name):
    return HttpResponse(f"The id you searched 2 is: {book_id},name is {book_name}.")

def book_path(request,book_path):
    return HttpResponse(f"the book path is: {book_path}")


