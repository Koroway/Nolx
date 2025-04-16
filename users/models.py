from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Місце"
        verbose_name_plural = "Місця"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ("member", "Користувач"),
        ("moderator", "Модератор"),
        ("admin", "Адмін"),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=9, choices=ROLES, default="member")
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
        ordering = ["username"]

    def __str__(self):
        return self.username