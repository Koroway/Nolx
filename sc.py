from ads.models import Category
from django.utils.text import slugify

for category in Category.objects.all():
    if not category.slug:
        category.slug = slugify(category.name)
        category.save()
