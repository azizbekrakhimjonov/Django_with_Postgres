from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.model

