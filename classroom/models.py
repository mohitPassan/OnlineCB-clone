from django.db import models

# Create your models here.

class Course(models.Model): #This class inherits from Model class in models module, which does the object mapping.
    name = models.CharField(max_length = 256)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name