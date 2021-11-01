from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='아이디 ')
    idnum = forms.CharField(label='주민등록번호 ')
    name = forms.CharField(label='이름 ')
    password = forms.CharField(label='비밀번호 ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인 ', widget=forms.PasswordInput)
    address = forms.CharField(label='주소 ')
    tel = forms.CharField(label='전화번호 ')
    email = forms.CharField(label='이메일 ')

    class Meta:
        model = User
        fields = ['username', 'idnum','name', 'password','password2','address','tel','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']