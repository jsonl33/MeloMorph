from django.db import models

class MusicFile(models.Model):
    file = models.FileField(upload_to='music_files/')

class VideoProject(models.Model):
    music_file = models.FileField(upload_to='music_files/')
    prompt = models.TextField()
