from django.shortcuts import render

from .models import Author
from .models import Quote
from .models import Infraction
import string


def index(request):
    author_names = [a.author_name for a in Author.objects.all()]

    return render(request, 'quotes/index.html', {'author_names': author_names})


def index_test(request):
    print('ok')
    # author_names = [a.author_name for a in Author.objects.all()]

    # return render(request, 'quotes/index.html', {'author_names': author_names})
    return 'Hello world'


def detail(request, author_name):
    author = Author.objects.filter(author_name=author_name).first()
    quote_list = author.quote_set.all()

    return render(request, 'quotes/detail.html', {'quote_list': quote_list})


def search_form(request):
    return render(request, 'quotes/search_form.html', {})


def search_quotes(request):
    if request.method == 'POST':
        word = request.POST['search_term']
        quote_list = Quote.objects.all()
        result = [q.quote_text for q in quote_list if q.search_quote(word)]

    return render(request, 'quotes/detail.html', {'quote_list': result})


def findequalmore(request, author_name):
    # if request.method == 'GET':
    #     word = request.GET['search_term']
    quote_list = Infraction.objects.all()
    result = [
        q.quote_text for q in quote_list if q.infractions_speed >= author_name]

    return render(request, 'quotes/toShow.html', {'quote_list': result})
