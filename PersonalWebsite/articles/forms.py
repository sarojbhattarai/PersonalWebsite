from django.forms import ModelForm
from articles.models import Category, Article


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ('slug',)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
    
