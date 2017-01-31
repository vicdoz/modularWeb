from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'aboutus.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})

def content_page_01(request):
    return render(request, 'content_page_01.html', {})
