from django.shortcuts import render
from django.http import JsonResponse
from api.models import List

def index(request):
    return JsonResponse({'data': list(List.objects.all().prefetch_related('user').values())})
