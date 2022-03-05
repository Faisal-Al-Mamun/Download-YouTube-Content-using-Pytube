# Now let's try to download a YouTube video in only audio format

from pytube import YouTube


def download_video(yt):
    # Filter all the audio files
    my_streams = yt.streams.filter(only_audio=True)
    
    print("Just type the itag number and press enter for downloading in your desired resolution.\n")
    for streams in my_streams:
       
        # print audio quality/itag/codec
        print(f"Audio itag : {streams.itag} Resolution : {streams.abr} File Type : {streams.mime_type}")
    
    # enter the itag value of resolution on which you want to downlaad the video
    input_itag = input("Enter itag Value : ")
    
    #get video using itag value
    audio = yt.streams.get_by_itag(input_itag)
    
    # finally download the YouTube video in audio format...
    audio.download()
    # audio.download(r"New path where you want to save the file")
    print("Audio is Downlading as ",yt.title+".webm")

#YouTube Video URL
link = "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed" 

# Create YouTube Object
yt = YouTube(link) 

# call the function
download_video(yt)

