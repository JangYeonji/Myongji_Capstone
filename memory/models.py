from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_addcon')
    name = models.CharField(max_length=200)
    work = models.CharField(max_length=200)
    mail = models.EmailField()
    tel = models.CharField(max_length=200)
    memo = models.CharField(max_length=200)
    birth = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('memory:address_detail', args=[str(self.id)])

class Schedule(models.Model):
    user2 = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_sche')
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    date = models.DateField()
    memo = models.TextField()
    anniversary = models.CharField(max_length=200) #초대받은사람


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user2.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('memory:schedule', args=[str(self.id)])

class Point(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_point')
    point = models.IntegerField()
    date = models.DateField()
    #sender = models.ForeignKey(Address.name,on_delete=models.CASCADE)
    #receiver = models.ForeignKey(Address.name,on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('memory:point', args=[str(self.id)])


class Money(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_money')
    money = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('memory:point', args=[str(self.id)])