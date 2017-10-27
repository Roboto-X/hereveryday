# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views  # blog

admin.autodiscover()

urlpatterns = [
    url(r'^$', blog_views.index, name='index'),  # blog index
    url(r'^blog/login/$', blog_views.login, name='login'),
    url(r'^blog/logout/$', blog_views.logout, name='logout'),
    url(r'^blog/article/(\d+)/$', blog_views.article, name="article"),  # blog add article
    url(r'^blog/add/$', blog_views.add, name="add"),  # blog add article
    url(r'^blog/about/$', blog_views.about, name="about"),  # blog add article


    url(r'^admin/', admin.site.urls),
]
