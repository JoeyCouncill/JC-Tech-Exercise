from django.http import HttpResponse


def Home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

