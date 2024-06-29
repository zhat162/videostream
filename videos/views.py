from django.shortcuts import render, get_object_or_404
from .models import Video
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Video
from .qos import measure_qos

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'videos/video_detail.html', {'video': video})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {
        'video': video,
    }
    return render(request, 'videos/video_detail.html', context)

@csrf_exempt
def update_qos(request, video_id):
    if request.method == 'POST':
        try:
            video = Video.objects.get(pk=video_id)
            data = request.POST
            video.latency = float(data.get('latency', 0))
            video.bit_rate = float(data.get('bit_rate', 0))
            video.sync_skew = float(data.get('sync_skew', 0))
            video.playback_jitter = float(data.get('playback_jitter', 0))
            video.packet_loss = float(data.get('packet_loss', 0))
            video.save()
            return JsonResponse({'status': 'success'})
        except Video.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Video not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})