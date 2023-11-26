from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def list(request):
    # Ваши данные из фейковой API
    data = [...]  # Замените на реальные данные
    return render(request, 'list.html', {'data': data})

def detail(request, object_id):
    # Ваши данные из фейковой API для объекта с ID object_id
    data = {}  # Замените на реальные данные
    return render(request, 'detail.html', {'data': data})

