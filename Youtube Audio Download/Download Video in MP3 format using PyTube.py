# Now let's try to download a YouTube video in only audio format

from pytube import YouTube


def download_video(yt):
    # Filter all the audio files
    audio = yt.streams.filter(only_audio=True).first()
    
    print("Audio is Downlading as ",yt.title+".wav")

    out_file = audio.download()
  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.wav'
    os.rename(out_file, new_file)

#YouTube Video URL
link = "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed" 

# Create YouTube Object
yt = YouTube(link) 

# call the function
download_video(yt)
