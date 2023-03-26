from django.db import models


class Specialization(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Vacation(models.Model):
    title = models.CharField(max_length=255)
    specialization = models.ManyToManyField('Specialization', blank=True)

    def __str__(self):
        return self.title
