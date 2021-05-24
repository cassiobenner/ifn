from django.shortcuts import render


def index(request):
    context = {
        'curso': 'curso de django freamwork',
        'outro': 'outro curso'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')