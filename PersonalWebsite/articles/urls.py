from django.urls import path
from articles.views import article_list, article_detail,\
                        add_article, add_category, update_article, search_articles

urlpatterns = [
    path('add_article/', add_article, name = 'AddArticle' ),
    path('update_article/<slug:slug>/', update_article, name='UpdateArticle' ),
    path('add_category/', add_category, name = 'AddCategory'),
    path('list/', article_list, name = 'ArticleList'),
    path('detail/<slug:slug>/', article_detail, name = 'ArticleDetail'),
    path('search_articles/', search_articles, name = 'SearchArticles'),
]