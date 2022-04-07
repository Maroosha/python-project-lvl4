from django.shortcuts import render


def index(request):
    "Index function."
    return render(request, 'index.html', context={
        'who': 'World',
    })
