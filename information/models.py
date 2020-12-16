from django.db import models
from django.utils import timezone

# Create your models here.
class Information(models.Model):
    WISH=(
        ('V', 'visited'),
        ('W', 'wish'),
        ('N', 'not yet'),
    )
    title=models.CharField(max_length=200)
    info_data=models.TextField()
    wish=models.CharField(max_length=1, choices=WISH, default='N')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Information, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    time=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text

