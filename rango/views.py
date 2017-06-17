from django.shortcuts import render
from django.http import HttpResponse
# Importing category model
from rango.models import Category, Page
# Create your views here.


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    # return HttpResponse("Rango says here is the about page.<br/><a
    # href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context={'About': 'About page'})


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        # .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an
        # exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # filter() will return a list of page objects or an empty
        # list
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
        # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
