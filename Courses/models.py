from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField('Имя', max_length=200, blank=True)
    description = models.CharField('Описание', max_length=12555, blank=True)
    hours = models.PositiveIntegerField('Количество часов', blank=True)
    date = models.DateField('Дата', blank=True)
    price = models.PositiveIntegerField('Цена', blank=True)
    count_themes = models.PositiveIntegerField('Количество тем', blank=True)

    class Meta:
        verbose_name = 'Курс',
        verbose_name_plural = 'Курсы'


class Task(models.Model):
    task = models.FileField('Файл', blank=True)
    description = models.CharField('Описание задания', max_length=12555, blank=True)


class Meta:
    verbose_name = 'Задание',
    verbose_name_plural = 'Задания'