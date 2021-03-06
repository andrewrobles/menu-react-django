from django.db import models
    
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class AuthCode(models.Model):
    value = models.CharField(max_length=8)

    def __str__(self):
        return self.value