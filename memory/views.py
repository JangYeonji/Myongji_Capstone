from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Address, Schedule, Point, Money
from django.contrib.auth.models import User
from .forms import ScheduleForm, AddressForm,PointForm, MoneyForm

def intro(request):
    pass
    return render(request, 'memory/main.html')

def contact(request):
    address = Address.objects.filter(user=request.user).order_by('name')
    return render(request,'memory/Memories_ContactAddress.html',{'address':address})

def create_address(request):
    user_obj = User.objects.get(username=request.user.get_username())
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            new_address = address_form.save(commit=False)
            new_address.user = user_obj
            new_address.save()
            return redirect('memory:Memories_ContactAddress')
    else:
        address_form = AddressForm()
    return render(request, 'memory/address_create.html',{'form':address_form})

class DetailAddress(DetailView):
    model = Address
    template_name_suffix = '_detail'

class UpdateAddress(UpdateView):
    model = Address
    fields = ['name','tel','work','mail','birth','memo']
    template_name_suffix = '_update'
    success_url = reverse_lazy('memory:Memories_ContactAddress')

class DeleteAddress(DeleteView):
    model = Address
    fields = ['name','tel','work','mail','birth','memo']
    template_name_suffix = '_delete'
    success_url = reverse_lazy('memory:Memories_ContactAddress')

def point(request):
    point = Point.objects.filter(user=request.user)
    money = Money.objects.filter(user=request.user)
    return render(request, 'memory/point.html',{'point':point,'money':money})

def create_point(request):
    user_obj = User.objects.get(username=request.user.get_username())
    if request.method == 'POST':
        point_form = PointForm(request.POST)
        if point_form.is_valid():
            new_point = point_form.save(commit=False)
            new_point.user = user_obj
            new_point.save()
            return redirect('memory:point')
    else:
        point_form = PointForm()
    return render(request, 'memory/point_create.html',{'form':point_form})

def create_money(request):
    user_obj = User.objects.get(username=request.user.get_username())
    if request.method == 'POST':
        money_form = MoneyForm(request.POST)
        if money_form.is_valid():
            new_money = money_form.save(commit=False)
            new_money.user = user_obj
            new_money.save()
            return redirect('memory:point')
    else:
        money_form = MoneyForm()
    return render(request, 'memory/money_create.html',{'form':money_form})


def schedule(request):
    schedule = Schedule.objects.filter(user2=request.user)
    return render(request, 'memory/schedule.html',{'schedule':schedule})


def calendar(request):
    schedule = Schedule.objects.filter(user2=request.user)
    return  render(request, 'memory/calendar.html',{'schedule':schedule})


def create_schedule(request):
    user_obj = User.objects.get(username=request.user.get_username())
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            new_schedule = schedule_form.save(commit=False)
            new_schedule.user2 = user_obj
            new_schedule.save()
            return redirect('memory:schedule')
    else:
        schedule_form = ScheduleForm()
    return render(request, 'memory/schedule_create.html',{'form':schedule_form})


class UpdateSchedule(UpdateView):
    model = Schedule
    fields = ['title','place','date','memo','anniversary']
    template_name_suffix = '_update'
    success_url = reverse_lazy('memory:schedule')

class DeleteSchedule(DeleteView):
    model = Schedule
    fields = ['title','place','date','memo','anniversary']
    template_name_suffix = '_delete'
    success_url = reverse_lazy('memory:schedule')

class DetailSchedule(DetailView):
    model = Schedule
    template_name_suffix = '_detail'

def event(request):
    pass
    return  render(request, 'memory/event.html')

