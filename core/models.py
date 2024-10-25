from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Cat(models.Model):
    owner = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.URLField()
    is_adopted = models.BooleanField(default=False)
    is_ill = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name} by {self.owner}'