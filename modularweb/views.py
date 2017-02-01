from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def contact(request):
    variables = {'pageName': 'Contact'}
    return render(request, 'contact.html', variables)

def about(request):
    variables = {'pageName': 'About us'}
    return render(request, 'aboutus.html', variables)


def gallery(request):
    variables = {'pageName': 'Gallery'}
    return render(request, 'gallery.html', variables)

def content_page_01(request):
    variables = {'pageName': 'Content'}
    return render(request, 'content_page_01.html', variables)
