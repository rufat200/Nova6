from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    image = models.ImageField(upload_to="publications/", null=True, blank=True)
    content = models.CharField(max_length=2500)
    is_archived = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='publications')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)