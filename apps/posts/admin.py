from django.contrib import admin
from apps.posts.models import Category,News

# Register your models here.
admin.site.register(Category)
admin.site.register(News)