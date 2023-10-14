from django.db import models

class AudioFile(models.Model):
    audio = models.FileField(upload_to='audio/')