from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1555, blank=True)
    image = models.ImageField(upload_to='news_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

class Discount(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1555, blank=True)
    image = models.ImageField(upload_to='discount_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

    def __str__(self):
        return self.title    

class Job(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=6000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    