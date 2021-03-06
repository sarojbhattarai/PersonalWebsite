from django.shortcuts import render, get_object_or_404,\
                            HttpResponseRedirect
from articles.models import Article, Category
from articles.forms import ArticleForm, CategoryForm
from django.urls import reverse
from django.db.models import Q
import random
from django.contrib.auth.decorators import login_required


# Create your views here.
def search_articles(request):
    articles = Article.objects.all().order_by('-published_on')
    query = request.GET.get('q')
    if query:
        queryset_list = articles.filter(
            Q(title__icontains=query)|
            Q(body__icontains=query)|
            Q(tags__name__in=[query])
            ).distinct()
        return render(request, 'articles/search_result.html', {"articles":queryset_list, 'query':query})
    return render(request, 'articles/search_result.html', {})

def article_list(request):
    articles = Article.objects.all().order_by('-published_on')
    front_featured_article = []
    featured_articles = articles.filter(is_featured=True)
    if featured_articles:
        front_featured_article = featured_articles[random.randint(0, len(featured_articles) - 1)]
    template_name = 'articles/list.html'
    context = {
        "articles": articles,
        "featured_articles":featured_articles,
        "front_featured_article": front_featured_article
    }
    return render(request, template_name, context)


def article_detail(request, slug=None):
    articles = Article.objects.all().order_by('-published_on')[:5]
    article = get_object_or_404(Article, slug=slug)
    template_name = 'articles/detail.html'
    context = {
        'article': article,
        'articles': articles
    }
    return render(request, template_name, context)

@login_required
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
@login_required
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

@login_required
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





def handler404(request):
        data = {}
        return render(request,'404.html', data)
 
def handler500(request):
        data = {}
        return render(request,'500.html', data)