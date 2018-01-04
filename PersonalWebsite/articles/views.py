from django.shortcuts import render, get_object_or_404,\
                            HttpResponseRedirect
from articles.models import Article, Category
from articles.forms import ArticleForm, CategoryForm
from django.urls import reverse
import random

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('-published_on')
    featured_articles = articles.filter(is_featured=True)
    front_featured_article = featured_articles[random.randint(0, len(featured_articles) - 1)]
    template_name = 'articles/list.html'
    context = {
        "articles": articles,
        "featured_articles":featured_articles,
        "front_featured_article": front_featured_article
    }
    return render(request, template_name, context)


def article_detail(request, slug=None):
    article = get_object_or_404(Article, slug=slug)
    template_name = 'articles/detail.html'
    context = {'article': article}
    return render(request, template_name, context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ArticleList', args=[]))
    else:
        form = ArticleForm()

    template_name = 'articles/new.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def update_article(request, slug=None):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ArticleDetail', kwargs={'slug':slug,}))
    else:
        form = ArticleForm(instance = article)

    template_name = 'articles/update.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ArticleList', args =[]))
    else:
        form = CategoryForm()
    template_name = 'articles/new_category.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)