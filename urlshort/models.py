from django.db import models


class UrlShort(models.Model):
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.original_url