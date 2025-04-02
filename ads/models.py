from django.db import models

from django.db import models

class Ad(models.Model):
    STATUS = [
        ("true", "Публіковано"),
        ("false", "Непубліковано"),
    ]

    name = models.CharField(max_length=3000)
    author = models.CharField(max_length=3000)
    price = models.IntegerField()
    description = models.CharField(max_length=3000)
    address = models.CharField(max_length=3000)
    is_published = models.CharField(max_length=5, choices=STATUS, default='false')
    image = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    age = models.IntegerField()
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE)
