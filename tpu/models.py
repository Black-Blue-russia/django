from django.db import models

# Create your models here.
from django.db import models

class building(models.Model):
    name = models.CharField(max_length = 120)
    description = models.TextField()

    def __str__(self):
        return self.name


