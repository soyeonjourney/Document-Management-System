from django.db import models


class Paper(models.Model):
    """Store paper information."""
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=256)
    conference = models.CharField(max_length=128)
    year = models.IntegerField()
    download_link = models.URLField(max_length=1024)
    abstract = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'paper-info'
        verbose_name_plural = 'paper-info'
        ordering = ['id']
