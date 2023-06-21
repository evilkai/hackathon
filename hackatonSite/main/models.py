from django.db import models
from .datedefs import setDate, getDate
from django.contrib.auth.models import Group
# Create your models here.


GROUP_CHOICES = []
GROUP_CHOICES.append(("All","All"))
for group in Group.objects.all():
    GROUP_CHOICES.append((group.name, group.name))



class Student(models.Model):
    global GROUP_CHOICES 

    fullname = models.CharField("Полное имя", max_length=30, default="")
    studentID = models.CharField("Студенческий билет", max_length=10, default="")
    year = models.CharField("Курс", max_length=1, default="")
    direction = models.CharField("Направление", max_length=40, default="")
    form = models.CharField("Форма обучения", max_length=20, default="")
    basis = models.CharField("Основание обучения", max_length=20, default="")
    country = models.CharField("Гражданство", max_length=20, default="")
    group = models.CharField('Отдел', max_length=10, choices=GROUP_CHOICES, default="All")
    registration = models.BooleanField('Статус регистрации',default=False,editable=False)


    id = models.AutoField(primary_key=True)


    def __str__(self):
        return self.fullname
    



    

class Ad(models.Model):
    global GROUP_CHOICES 

    title = models.CharField('Название', max_length=50, default="Новость ")
    description = models.TextField('Описание', max_length=500, default="")
    date = models.DateField('Дата публикации', default=getDate(),blank=True, editable=False)
    
    id = models.AutoField(primary_key=True)



    def __str__(self):
        return self.title
    
class Telegram(models.Model):

    tgID = models.CharField('ID', max_length=50, default="")
    
    id = models.AutoField(primary_key=True)



    def __str__(self):
        return self.tgID