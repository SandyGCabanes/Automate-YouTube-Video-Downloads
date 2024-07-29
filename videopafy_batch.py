# sandy.g.cabanes
# Title: videos using pafy
# Description: video downloaded as mp4 in C:/temp/video folder
# Date: July 18, 2024
# ------------------------------------------------------------

print("Initializing...")
import time
import yt_dlp
from urllib.parse import urlparse, parse_qs

def is_valid_youtube_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch' and 'v' in parse_qs(parsed_url.query):
            return True
        elif parsed_url.path.startswith('/playlist'):
            return True
    elif parsed_url.netloc == 'youtu.be':
        return True
    return False

def download_video(url, save_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'quiet': True,
        'no_color': True,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    if not is_valid_youtube_url(url):
        print(f"Invalid YouTube URL: {url}")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

print("Reminder: create a txt file in C:/temp/video folder, with list of addresses")
time.sleep(2)
print("Name it as list_of_addresses.txt")
time.sleep(5)

# opening the file in read mode
my_file = open("C:/temp/video/list_of_addresses.txt", "r")

# reading the file
data = my_file.read()

# splitting the text when newline ('\n') is seen.
listofa = data.split("\n")
print(listofa)
my_file.close()

numitems = len(listofa)
print(f"There are {numitems} files.")

for i, url in enumerate(listofa, 1):
    video_save_location = "C:/temp/video"
    download_video(url.strip(), video_save_location)
    print(f"{i} of {numitems}")

print("Batch of videos downloaded. Check your C:/temp/video folder.")
print("Window closing in 5 seconds")
time.sleep(5)
