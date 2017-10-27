# coding:utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .constants import constants
from .util import util


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'标题', max_length=50)
    content = models.TextField(u'内容', max_length=50000)
    img = models.FileField(u'照片', upload_to=constants.UPLOAD_TO + util.current_date())

    def __str__(self):
        return self.title
