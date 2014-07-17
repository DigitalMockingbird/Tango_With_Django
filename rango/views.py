# from django.shortcuts import render
# from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category
from rango.models import Page

# def encode_url(str):
#     return str.replace(' ', '_')
#
# def decode_url(str):
#     return str.replace(' ', '_')

def remove_space(str):
    return str.replace(' ', '')

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    top_viewed_pages = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'top_viewed_pages': top_viewed_pages}

    for category in category_list:
        category.url = remove_space(category.name)

    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', context)

def cake(request):
    context = RequestContext(request)
    context_dict = {'cake_type': "black forest"}
    return render_to_response('rango/cake.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)
    # category_name = decode_url(category_name_url)
    context_dict = {'category_name': category_name_url}

    try:
        category = Category.objects.get(name=category_name_url)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)