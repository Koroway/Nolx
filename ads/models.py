from django.core.validators import MinLengthValidator
from django.db import models

from users.models import User


class Category(models.Model):
    slug = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(5)])
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="ads/", null=True, blank=True)

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

