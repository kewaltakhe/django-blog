from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='')
    body = models.TextField(default='')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])   #/post/whatever-id
    # this method returns the address/ url of each post object when called on that particular object


