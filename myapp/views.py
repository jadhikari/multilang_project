from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')


def switch_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in ['en', 'jp']:
            request.session['django_language'] = language
    # Redirect to the same page or a specific page
    return redirect(request.META.get('HTTP_REFERER', '/'))

