from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name