from django.contrib import admin
from articles.models import Article, Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    '''
        Admin View for Article
    '''
    list_display = ('title', 'category', 'author', 'slug',)
    list_filter = ('category',)
    prepopulated_fields = {"slug": ("title",)}



class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    list_display = ('title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Article, ArticleAdmin)