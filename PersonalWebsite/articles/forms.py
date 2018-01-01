from django.forms import ModelForm
from articles.models import Category, Article


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = '__all__'