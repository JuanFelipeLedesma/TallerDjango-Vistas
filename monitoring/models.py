from django.db import models

class Measurement(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.value}"
