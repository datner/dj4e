from django.db import models

# Create your models here.

# unesco_category, unesco_iso, unesco_region, unesco_site, and unesco_state

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)

class Iso(models.Model):
    name = models.CharField(max_length=128)

class Region(models.Model):
    name = models.CharField(max_length=128)


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

