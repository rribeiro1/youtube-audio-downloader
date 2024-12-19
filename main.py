# /// script
# dependencies = [
#     "yt_dlp",
#     "youtube-search-python",
# ]
# ///

import yt_dlp
import urllib.request
import urllib.parse
import re

# Define the songs to download and the destination folder for the audio files.
destination_folder = "./"
songs = [
    "Gabriel Guedes - Santo Pra Sempre",
]

def download_audio(song, destination_folder):
    encoded_query = urllib.parse.quote(song)
    search_url = "https://www.youtube.com/results?search_query=" + encoded_query
    html = urllib.request.urlopen(search_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    # Get the first video id if found.
    if video_ids:
        print("https://www.youtube.com/watch?v=" + video_ids[0])
        video_url = "https://www.youtube.com/watch?v=" + video_ids[0]
    else:
        print("No video found.")
        return

    try:
        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{destination_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            print("Downloading audio for song: ", song)
            ydl.download([video_url])
    except Exception as e:
        print(f"Error: {e}")


# Entry point.
for song in songs:
    download_audio(song, destination_folder)
print("Download completed!")
