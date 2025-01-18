from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)  
    likes = models.IntegerField(default=0)  
    dislikes = models.IntegerField(default=0)  

    def __str__(self):
        return str(self.title) if self.title else str(self.image)
