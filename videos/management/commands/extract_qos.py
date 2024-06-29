# videos/management/commands/extract_qos.py
import subprocess
from django.core.management.base import BaseCommand
from videos.models import Video

class Command(BaseCommand):
    help = 'Extract QoS parameters for videos'

    def handle(self, *args, **kwargs):
        videos = Video.objects.all()
        for video in videos:
            video_path = video.video_file.path
            try:
                # Extract duration
                duration_cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
                duration = float(subprocess.check_output(duration_cmd, shell=True).strip())

                # Extract bit rate
                bitrate_cmd = f'ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
                bit_rate = float(subprocess.check_output(bitrate_cmd, shell=True).strip()) / 1000  # Convert to kbps

                # For simplicity, we'll use placeholders for other parameters
                # In a real scenario, these would be computed or measured
                latency = 0.1  # Placeholder
                sync_skew = 0.2  # Placeholder
                playback_jitter = 0.1  # Placeholder
                packet_loss = 0.0  # Placeholder

                video.latency = latency
                video.bit_rate = bit_rate
                video.sync_skew = sync_skew
                video.playback_jitter = playback_jitter
                video.packet_loss = packet_loss
                video.duration = duration
                video.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully extracted QoS for {video.title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error extracting QoS for {video.title}: {e}'))
