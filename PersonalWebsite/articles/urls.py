from django.urls import path
from articles.views import article_list, article_detail

urlpatterns = [
    path('list/', article_list, name = 'ArticleList'),
    path('detail/<slug:slug>/', article_detail, name = 'ArticleDetail'),
]