from django.db import models
from django.utils import timezone


class Product(models.Model):
    creator = models.CharField(max_length=100)  # Создатель продукта
    name = models.CharField(max_length=100)  # Название продукта
    start_date = models.DateTimeField(default=timezone.now)  # Дата и время старта


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому относится урок
    title = models.CharField(max_length=100)  # Название урока
    video_link = models.URLField()  # Ссылка на видео


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому относится группа
    name = models.CharField(max_length=100)  # Название группы
    min_users = models.PositiveIntegerField()  # Минимальное количество пользователей в группе
    max_users = models.PositiveIntegerField()  # Максимальное количество пользователей в группе

    def is_full(self):
        return self.user_set.count() >= self.max_users  # Проверка, полная ли группа


class User(models.Model):
    groups = models.ManyToManyField(Group)  # Группы, в которых состоит пользователь


