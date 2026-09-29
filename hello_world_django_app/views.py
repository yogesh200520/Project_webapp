from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("<h6>Run using docker compose</h6>")


def hello_world(request):
    return HttpResponse("<html><body>Hello World</body></html>")


def health_check(request):
    return JsonResponse({"status": "healthy"})
