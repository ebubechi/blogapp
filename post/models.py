from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=130)
    content = models.TextField()

    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id':self.id})

    class Meta:
        ordering = ['-id','-timestamp','-updated']























