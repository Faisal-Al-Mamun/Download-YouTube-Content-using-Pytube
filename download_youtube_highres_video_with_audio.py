from pytubefix import YouTube
from pytubefix.cli import on_progress

import os
import re
from moviepy import VideoFileClip, AudioFileClip

url = "https://www.youtube.com/watch?v=eWd4cSUsDHg"

yt = YouTube(url, on_progress_callback=on_progress)
print("Title:", yt.title)

# Download highest quality video-only stream (usually .mp4, no audio)
video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4").order_by("resolution").desc().first()
# Download highest quality audio-only stream (usually .webm or .mp4)
audio_stream = yt.streams.filter(adaptive=True, only_audio=True).order_by("abr").desc().first()

if not video_stream or not audio_stream:
    print("Could not find suitable video or audio streams.")
    exit(1)

print("Downloading video...")
video_path = video_stream.download(filename="temp_video.mp4")
print("Downloading audio...")
audio_path = audio_stream.download(filename="temp_audio.webm")

# Sanitize the title for a safe filename
safe_title = re.sub(r'[\\/*?:"<>|,]', "_", yt.title)
output_filename = safe_title.replace(" ", "_") + "_highres.mp4"
print("Merging video and audio...")

# Merge video and audio using moviepy
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)
final_clip = video_clip.with_audio(audio_clip)
final_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

# Clean up temp files
video_clip.close()
audio_clip.close()
os.remove(video_path)
os.remove(audio_path)

print(f"Download and merge complete: {output_filename}")