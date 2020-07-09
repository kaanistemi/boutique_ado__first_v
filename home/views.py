from django.shortcuts import render

# Create your views here.


def index(request):
    """A view return to index page"""

    return render(request, 'home/index.html')
    