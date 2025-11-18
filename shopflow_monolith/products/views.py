from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def product_list_view(request):
    data = {
        'message': 'success',
        'status': 200
    }

    return JsonResponse(data)
