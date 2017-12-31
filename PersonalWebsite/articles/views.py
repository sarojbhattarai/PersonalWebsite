from django.shortcuts import render, get_object_or_404
from articles.models import Article, Category
# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    template_name = 'articles/list.html'
    context = {"articles": articles}
    return render(request, template_name, context)


def article_detail(request, slug=None):
    article = get_object_or_404(Article, slug=slug)
    template_name = 'articles/detail.html'
    context = {'article': article}
    return render(request, template_name, context)