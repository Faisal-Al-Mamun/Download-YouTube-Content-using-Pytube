# Let's first fetch the video meta data like video title, video length, total views etc.

from pytube import YouTube

# Function takes YouTube object as argument
def video_info(yt):
    print("Title :", yt.title)
    print("Video Length :", yt.length,"Seconds")
    print("Total Views :", yt.views)
    print("Published Date :", yt.publish_date)
    print("Thumbnail Url :", yt.thumbnail_url)
    print("Is Age Restricted :", yt.age_restricted)
    print("Video Rating :", yt.rating)

#YouTube Video URL
link = "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed" 
yt = YouTube(link) # Create YouTube Object

# call the function
video_info(yt)