from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'word_generator/index.html')

def generate(request):
    request.session['random_word'] = get_random_string(length=13)
    request.session['counter'] += 1
    return render(request, 'word_generator/index.html')

def reset(request):
    del request.session['counter']
    return redirect('/')