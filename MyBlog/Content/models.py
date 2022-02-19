from tkinter import CASCADE
from django.db import models
from django.forms import CharField


class Category (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name





class Blog (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True ,null=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField()
    


    def __str__(self):
        return self.title
    def __str__(self):
        return self.content    
class Comment (models.Model):
    post = models.ForeignKey(Blog,related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
 

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)