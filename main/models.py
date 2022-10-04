from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return f'{self.name} --> {self.parent}' if self.parent else f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')

    preview = models.ImageField(upload_to='images/' , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner}--> {self.title}'

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'
