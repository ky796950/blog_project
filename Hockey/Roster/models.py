from django.db import models
from django.urls import reverse
from django.utils import timezone
 
# Create your models here.
class Post(models.Model):
    """Model to post blog text"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
 
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
 
    def __str__(self):
        return self.title
 
 
class Comment(models.Model):
    """Model to comment on posts."""
    post = models.ForeignKey('Roster.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
 
    def approve(self):
        self.approved_comment = True
        self.save()
 
    def get_absolute_url(self):
        return reverse("post_detail")
 
    def __str__(self):
        return self.text