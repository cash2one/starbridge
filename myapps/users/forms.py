from django import forms
from django.contrib import auth
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import CustomUser


# class LoginUserForm(AuthenticationForm):
#
#      def __init__(self, *args, **kwargs):
#          super(LoginUserForm, self).__init__(*args, **kwargs)
class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'账 号', error_messages={'required':u'账号不能为空'},
        widget=forms.TextInput(attrs={'placeholder': u'账号','class':'form-control'}))
    password = forms.CharField(label=u'密 码', error_messages={'required':u'密码不能为空'},
        widget=forms.PasswordInput(attrs={'placeholder': u'密码', 'class':'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        super(LoginUserForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        """ 给form类自定义验证规则，如果想要重用验证机制，可以单独创建新的字段类，重新写它的验证方法。
            一般的可以直接在form类加入clean_字段名的方法，Django会自动查找以clean_开头的函数名，并会在
            验证该字段的时候，运行这个函数"""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'账号密码不匹配')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'此账号已被禁用')
        return self.cleaned_data     # 在自定义的验证函数中，我们必须显示的返回字段名的内容，否则会带来表单数据丢失。

    def get_user(self):
        return self.user_cache

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','email']
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ForgetPasswordForm(forms.Form):
    username = forms.CharField(label=u'用户名')
    email = forms.EmailField(label=u'邮 箱')

class ChangePasswordForm(forms.Form):
    old_password  = forms.CharField(label=u'旧 密 码', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=u'新 密 码', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=u'确 认 密 码', widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    new_password1 = forms.CharField(label=u'密 码', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=u'确 认 密 码', widget=forms.PasswordInput)