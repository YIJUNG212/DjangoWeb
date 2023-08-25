from django import forms
from django.contrib.auth.forms import UserCreationForm
#我已經在models.py裡客製化webuser資料表了,所以這裡應該是要改用那個
from .models import webUser
#from django.contrib.auth.models import User
#註冊類別
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = webUser
        fields = ('username', 'email', 'password1', 'password2')

#登入類別
class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
#訂立一個product 新增用的表格
from .models import product
class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"