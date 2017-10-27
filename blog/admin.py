# coding:utf-8
from django.contrib import admin
from .models import Article


class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'img',)


admin.site.register(Article)
