from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # Constructing a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the
    # template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
    # Returning a rendered response to send to the client.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page.<br/><a href='/rango/'>Index</a>")
