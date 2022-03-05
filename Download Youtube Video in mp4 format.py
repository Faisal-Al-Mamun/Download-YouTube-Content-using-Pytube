# Now let's try to download a YouTube video in mp4 format along with audio

from pytube import YouTube

def download_video(yt):
    # filter mp4 streams from object
    my_streams = yt.streams.filter(file_extension='mp4') # use only_video=True parameter for downloading only the video
    
    print("Just type the itag number and press enter for downloading in your desired resolution.\n")
    for streams in my_streams:
       
        # print itag, resolution and codec format of mp4 streams
        print(f"Video itag : {streams.itag} Resolution : {streams.resolution} File Type : {streams.mime_type}")
    
    # enter the itag value of resolution on which you want to downlaad the video
    input_itag = input("Enter itag Value : ")
    
    #get video using itag value
    video = yt.streams.get_by_itag(input_itag)
    
    # finally download the YouTube video...
    video.download()
    print("Video is Downlading as ",yt.title+".mp4")

#YouTube Video URL
link = "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed" 

# Create YouTube Object
yt = YouTube(link) 

# call the function
download_video(yt)
