from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', default='path/to/default_thumbnail.jpg')
    video_file = models.FileField(upload_to='videos/')
    is_portrait = models.BooleanField(default=False)
    latency = models.FloatField(null=True, blank=True)
    bit_rate = models.FloatField(null=True, blank=True)
    sync_skew = models.FloatField(null=True, blank=True)
    playback_jitter = models.FloatField(null=True, blank=True)
    packet_loss = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
