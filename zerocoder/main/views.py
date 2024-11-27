from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django<h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django<h1>")

def data(request):
    return HttpResponse("<h1>Это страница Data<h1>")  # Контент для /data

def test(request):
    return HttpResponse("<h1>Это страница Test<h1>")  # Контент для /test