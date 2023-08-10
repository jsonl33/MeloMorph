from django.shortcuts import render, redirect
from pydub import AudioSegment
from django.http import JsonResponse

from .forms import MusicFileForm, VideoProjectForm

def upload(request):
    if request.method == 'POST':
        form = MusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save()
            duration = analyze_music_file(music_file.file.path)
            return JsonResponse({'success': True, 'duration': duration})
    else:
        form = MusicFileForm()
    return render(request, 'upload.html', {'form': form})

def analyze_music_file(file_path):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio)  # 음악 파일의 길이 (밀리초)
    # 여기에서 추가 분석을 수행할 수 있습니다.
    return duration

def create_video(request):
    if request.method == 'POST':
        form = VideoProjectForm(request.POST, request.FILES)
        if form.is_valid():
            video_project = form.save()
            # 여기에서 영상 생성 로직을 추가할 수 있습니다.
            return redirect('video_success')
    else:
        form = VideoProjectForm()
    return render(request, 'create_video.html', {'form': form})

from django.shortcuts import render

def create_music(request):
    return render(request, 'create_music.html')




