# coding:utf-8
from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label="用户名", max_length=50, min_length=1)
    password = forms.CharField(label="密码",widget=forms.PasswordInput, max_length=50, min_length=1)


class AddForm(forms.Form):
    title = forms.CharField(label="标题", max_length=50, min_length=1)
    content = forms.CharField(label="文章", widget=forms.Textarea, max_length=50000, min_length=1)
    img = forms.FileField(label="照片", )
