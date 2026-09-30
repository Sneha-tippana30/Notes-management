from django.db import models

# Create your models here.


class Question(models.Model):
    category = models.CharField(max_length=100)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    

    def __str__(self):
        return self.question