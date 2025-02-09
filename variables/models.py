from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return '{}'.format(self.name)