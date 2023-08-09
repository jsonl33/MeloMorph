from django import forms
from .models import MusicFile
from .models import VideoProject

class MusicFileForm(forms.ModelForm):
    class Meta:
        model = MusicFile
        fields = ('file',)
        
class VideoProjectForm(forms.ModelForm):
    class Meta:
        model = VideoProject
        fields = ('music_file', 'prompt')
