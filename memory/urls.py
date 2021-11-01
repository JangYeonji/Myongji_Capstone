from django.urls import path
from .views import *   # views.py 내의 모든 객체, 함수 포함
from django.contrib.auth import views as auth_views

app_name = 'memory'

urlpatterns = [
    path('', intro, name='main'),

    path('contactAddress', contact, name='Memories_ContactAddress'),
    path('addcreate/', create_address, name='addcreate'),
    path('adddetail/<int:pk>',DetailAddress.as_view(),name='adddetail'),
    path('addupdate/<int:pk>',UpdateAddress.as_view(),name='addupdate'),
    path('adddelete/<int:pk>', DeleteAddress.as_view(), name='adddelete'),

    path('point', point, name='point'),
    path('pocreate/',create_point, name='pocreate'),

    path('mocreate/',create_money, name='mocreate'),

    path('schedule', schedule, name='schedule'),
    path('sccreate/', create_schedule, name='sccreate'),
    path('scdetail/<int:pk>',DetailSchedule.as_view(),name='scdetail'),
    path('scupdate/<int:pk>', UpdateSchedule.as_view(), name='scupdate'),
    path('scdelete/<int:pk>', DeleteSchedule.as_view(), name='scdelete'),

    path('event', event, name='event'),
    path('calendar', calendar, name='calendar'),
]
