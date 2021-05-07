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

    def __str__(self):
        return "{} на {} тем".format(self.name , self.count_themes)
    


class Task(models.Model):
    name = models.CharField('Название задания', max_length=255, blank=True)
    task = models.FileField('Файл', blank=True)
    description = models.CharField('Описание задания', max_length=12555, blank=True)


    class Meta:
        verbose_name = 'Задание',
        verbose_name_plural = 'Задания'


    def __str__(self):
        return self.name
    


