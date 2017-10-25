# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views  # blog
admin.autodiscover()

urlpatterns = [
    url(r'^$', blog_views.index, name='index'),  # blog index
    url(r'^article/(\d+)/$', blog_views.article, name="article"),  # blog add article
    url(r'^add/$', blog_views.add, name="add"),  # blog add article


    url(r'^admin/', admin.site.urls),
]
