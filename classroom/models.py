from django.db import models

# Create your models here.

class Course(models.Model): #This class inherits from Model class in models module, which does the object mapping.
    name = models.CharField(max_length = 256)
    price = models.FloatField()
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete = models.CASCADE)
    recommended = models.BooleanField(default = False)
    contents = models.ManyToManyField('Content')

    def __str__(self):
        return self.name

class Instructor(models.Model):
    photo = models.URLField(null = True, blank = True)
    name = models.CharField(max_length = 256)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_CHOICES = [
        ('pdf', 'PDF'),
        ('youtube', 'Youtube Videos'),
        ('image', 'Image'),
    ]
    name = models.CharField(max_length = 256)
    content_type = models.CharField(max_length = 256, choices = CONTENT_CHOICES)

    def __str__(self):
        return self.name