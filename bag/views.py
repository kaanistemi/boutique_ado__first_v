from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """A view return to bag page"""

    return render(request, 'bag.html')
    