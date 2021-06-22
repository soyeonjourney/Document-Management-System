from django.db import models


class Collection(models.Model):
    """Store user collection."""
    user_id = models.BigIntegerField()
    paper = models.ForeignKey('library.Paper', on_delete=models.CASCADE)
    collection_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.collection_time, self.user_id, self.paper.title

    class Meta:
        verbose_name = 'user-collection'
        verbose_name_plural = 'user-collection'
        ordering = ['user_id', 'collection_time']
