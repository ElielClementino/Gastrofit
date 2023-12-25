from django.http import JsonResponse


def hello(request):
    hello = {"hello": "hello"}
    return JsonResponse(hello)
