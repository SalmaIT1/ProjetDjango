from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy






class PostModel(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} by {self.author}, created on {self.created_date}, published on {self.published_date}, image: {self.image}, text: {self.text}"

    


class Comment(models.Model):
    post = models.ForeignKey( PostModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    date_added =models.DateField(null=True,default=date.today)
    
 

