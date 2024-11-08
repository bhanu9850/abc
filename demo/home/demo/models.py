from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length= 25)
    author = models.CharField(max_length= 25)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author
    
    