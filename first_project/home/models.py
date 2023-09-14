from django.db import models

# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=50)
    features = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField(max_length=50)
    starrating = models.IntegerField(default=0) # can use without max_length

    def __str__(self):
        return str(self.id) + ', ' + self.name