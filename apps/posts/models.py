from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="news_category")
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to = "news/")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

        

   

