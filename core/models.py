from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to="imgs/")
    category_order = models.IntegerField(default=1000)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("category_order", "category_title")

    def __str__(self):
        return self.category_title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=300)
    news_author = models.CharField(max_length=100, default="News")
    news_image = models.ImageField(upload_to="imgs/")
    news_detail = models.TextField()
    news_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.news_title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
