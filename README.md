<h1>Pytube</h1>

<h1>pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.</h1>

<h3> First install pytube on your pc using 'pip install pytube' command.</h3>
<h3> Then You are ready to go.</h3>
<h3> You can easily dowwnlad YouTube videos in various format without using any third party software.</h3>

# Download YouTube Content using Pytubefix

> **Note:**  
> The original [pytube](https://github.com/pytube/pytube) project is no longer maintained and does not work reliably due to YouTube site changes.  
> This repository uses [pytubefix](https://github.com/JuanBindez/pytubefix), a maintained fork, to enable YouTube video and playlist downloading.

## Features

- Download YouTube videos in MP4 format (with or without audio)
- Download high-resolution YouTube videos (merging best video and audio)
- Download YouTube audio only (MP3 or original format)
- Download entire YouTube playlists
- Fetch and display YouTube video metadata (title, views, etc.)

## Requirements

- Python 3.7+
- [pytubefix](https://github.com/JuanBindez/pytubefix)
- [moviepy](https://github.com/Zulko/moviepy) (for merging video and audio)

Install dependencies with:
```sh
pip install -r requirements.txt
```

## Scripts

| Script Name                        | Description                                      |
|------------------------------------|--------------------------------------------------|
| `download_youtube_video_mp4.py`    | Download YouTube video in MP4 format             |
| `download_youtube_audio_only.py`   | Download YouTube audio only (original format)    |
| `download_youtube_audio_mp3.py`    | Download YouTube audio and save as MP3           |
| `download_youtube_playlist.py`     | Download all videos in a YouTube playlist        |
| `download_youtube_highres_video.py`| Download and merge highest quality video+audio   |
| `youtube_video_info.py`            | Fetch and display YouTube video metadata         |

## Usage

1. **Clone this repository:**
    ```sh
    git clone https://github.com/yourusername/Download-YouTube-Content-using-Pytube.git
    cd Download-YouTube-Content-using-Pytube
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the desired script:**
    ```sh
    python download_youtube_highres_video.py
    ```
    *(Edit the script to change the YouTube URL as needed.)*

## Notes

- For high-resolution downloads, the script merges the best video and audio streams using `moviepy`.
- Output filenames are sanitized for Windows compatibility.
- Make sure you comply with YouTube's Terms of Service when downloading content.

## License

This project is licensed under the MIT License.

---

