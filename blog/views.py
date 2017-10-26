# coding:utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from blog.models import Article, User
from .forms import AddForm, LoginForm
from .util import util
from .constants import constants


def __is_login(request):
    try:
        name = request.session["name"]
    except KeyError:
        name = None
    if name is not None:
        pass
    else:
        form = LoginForm()
        return render(request, constants.HTML_LOGIN, {'form': form})


def index(request):
    titles = Article.objects.all().only("id", "title")
    return render(request, constants.HTML_INDEX, {"titles": titles})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(name=name)
            except User.DoesNotExist:
                user = None

            if user is not None and user.password == password:
                request.session["name"] = name
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, constants.HTML_LOGIN, {'form': form})
        else:
            return render(request, constants.HTML_LOGIN, {'form': form})
    else:
        form = LoginForm()
        return render(request, constants.HTML_LOGIN, {'form': form})


def logout(request):
    try:
        del request.session['name']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('index'))


def article(request, article_id):
    article_by_id = Article.objects.get(id=article_id)
    article_by_id.img.name = util.convert_readable_img(article_by_id.img.name)
    return render(request, constants.HTML_ARTICLE, {"article": article_by_id})


def add(request):
    # __is_login(request)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            file = request.FILES.get('img')
            Article.objects.get_or_create(title=title, content=content, img=file)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, constants.HTML_ADD, {'form': form})
    else:
        form = AddForm()
        return render(request, constants.HTML_ADD, {'form': form})
