from django.db import models


class AuthorPaperCount(models.Model):
    """Store author paper count."""
    author = models.CharField(max_length=128)
    count = models.IntegerField()
    conference = models.CharField(max_length=256)
    year = models.IntegerField()

    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name = 'author-ranking'
        verbose_name_plural = 'author-ranking'
        ordering = ['id']
