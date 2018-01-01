from django.urls import path
from articles.views import article_list, article_detail,\
                        add_article, add_category

urlpatterns = [
    path('add_article/', add_article, name = 'AddArticle' ),
    path('add_category/', add_category, name = 'AddCategory'),
    path('list/', article_list, name = 'ArticleList'),
    path('detail/<slug:slug>/', article_detail, name = 'ArticleDetail'),
]