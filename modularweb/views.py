from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


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


# HTTP Error 400
def page_not_found_404(request):
    response = render_to_response(
        '404.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 400

    return response

