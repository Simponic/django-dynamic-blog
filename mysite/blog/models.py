from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=30)
    content = models.TextField()
    posted = models.DateTimeField('date published')
    image_path = models.CharField(max_length=100)
    image_alt = models.CharField(max_length=200)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    posted = models.DateTimeField('date published')
