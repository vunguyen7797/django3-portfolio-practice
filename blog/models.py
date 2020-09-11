from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    date = models.DateField()

    # turn default name to object title
    def __str__(self):
        return self.title
