# sandy.g.cabanes
# Title: videos using pafy
# Description: video downloaded as mp4 in C:/temp/video folder
# Date: July 13, 2024  (not working -- see ytdlp version)
# ------------------------------------------------------------

print ("Initializing...")
import pafy
import time
import yt_dlp as youtube_dl


#def download_video(url, save_path, output_path): #for both video and audio
def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'quiet': True,
        'no_color': True,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video = pafy.new(url, ydl_opts=ydl_opts)
        best = video.getbest()
        best.download(filepath=save_path)

    #audio = video.getbestaudio()
    #audio.download(output_path)


# Input list of http addresses as a list

print ("Reminder: create a txt file in C:/temp/video folder, with list of addresses")
time.sleep (2)
print ("Name it as list_of_addresses.txt")
time.sleep (5)

# opening the file in read mode, rtf will not work
my_file = open("C:/temp/video/list_of_addresses.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
listofa = data.split("\n")
print(listofa)
my_file.close()

numitems = len(listofa)
print ("There are ", numitems, " files.")


i = 0
while i < len(listofa):

    url = listofa[i]

    video_save_location = "C:/temp/video"

    download_video(url, video_save_location)

    print (i+1, " of ", numitems)

    i = i+1


print ("Batch of videos downloaded.  Check your C:/temp/video folder.")
print ("Window closing in 5 seconds")
time.sleep (5)

