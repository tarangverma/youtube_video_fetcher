from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnails = models.JSONField()
    video_id = models.CharField(max_length=50, unique=True)

    class Meta:
        indexes = [models.Index(fields=["published_at"])]
        ordering = ["-published_at"]
