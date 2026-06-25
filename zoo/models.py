from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aviary(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Номер')

    def __str__(self):
        return str(self.number)


class Animals(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес')
    aviaryID = models.ForeignKey(Aviary, on_delete=models.CASCADE, verbose_name='Номер Загона')
    photoPath = models.ImageField(upload_to='photos/')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    age = models.IntegerField()
