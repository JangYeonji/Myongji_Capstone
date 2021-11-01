from django.contrib.auth.models import User
from django import forms
from .models import Schedule, Address, Point, Money


class ScheduleForm(forms.ModelForm):
    title = forms.CharField(label='제목 ')
    date = forms.DateField(label='일정 ')
    place = forms.CharField(label='장소 ')
    memo = forms.CharField(label='내용 ', widget=forms.Textarea)
    anniversary = forms.CharField(label='초대받은 사람 ')

    class Meta:
        model = Schedule
        fields = ["title", "date", "place", "memo", "anniversary"]


class AddressForm(forms.ModelForm):
    name = forms.CharField(label='이름 ')
    tel = forms.CharField(label='연락처 ')
    work = forms.CharField(label='소속 ')
    mail = forms.CharField(label='이메일 ')
    birth = forms.DateField(label='생일 ')
    memo = forms.CharField(label='메모 ', widget=forms.Textarea)

    class Meta:
        model = Address
        fields = ["name", "tel", "work", "mail", "birth", "memo"]


class PointForm(forms.ModelForm):
    point = forms.IntegerField(label='포인트 ')
    date = forms.DateField(label='날짜 ')
    sender = forms.CharField(label='보낸사람 ')
    receiver = forms.CharField(label='받는사람 ')

    class Meta:
        model = Point
        fields = ["point", "date", "sender", "receiver"]


class MoneyForm(forms.ModelForm):
    money = forms.IntegerField(show_hidden_initial=True)

    class Meta:
        model = Money
        fields=["money"]