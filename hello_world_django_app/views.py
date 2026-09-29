from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("<h1>Its Done</h1>")


def hello_world(request):
    return HttpResponse("<html><body>Hello World</body></html>")


def health_check(request):
    return JsonResponse({"status": "healthy"})
