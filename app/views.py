from django.http import Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    if (request.method == "GET"):
        response = {
            "message": "Hello, World!!"
        }
        return JsonResponse(response)
    else:
        return Http404
