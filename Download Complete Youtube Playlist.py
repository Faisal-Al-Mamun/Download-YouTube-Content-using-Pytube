# Now let's try to download a Complete YouTube Playlist

from pytube import Playlist


def download_playlist(ytp):
    # Print Playlist Title..
    print("Playlist Title :",ytp.title)
    
    # get videos of playlist..
    for video in ytp.videos:
       try:
           #download all videos in best resolution
           video.streams.first().download(video.title)
       except Exception as e:
           print(e,type(e))
         
    print("Playlist is Downloaded...")

#YouTube Playlist URL
link = "https://www.youtube.com/playlist?list=PLbcjjday_tJNoxrX5NtsstcZbTKD3lLn6" 

# Create YouTube Object
ytp = Playlist(link) 

# call the function
download_playlist(ytp)

