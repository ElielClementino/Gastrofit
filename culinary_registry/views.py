from django.shortcuts import render
from django.http import JsonResponse

def hello(request):
    hello = {"hello":"hello"}
    return JsonResponse(hello)