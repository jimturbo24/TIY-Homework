from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Article

def index(request):
    resp_string = "<ul>\n"
    recent_articles = Article.objects.order_by('-publish_date')[:5]
    # templ = loader.get_template('simplecontent/articles_index.html')
    context = {'recent_articles': recent_articles}
    return render(request, 'simplecontent/articles_index.html', context)

def view_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("No such article!")
    context = {'article': article}

    return render(request, 'simplecontent/article_details.html', context)
