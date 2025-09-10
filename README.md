# YouTube Downloader App
A Python script using `pytubefix` and `ffmpeg` to download audio or video content from YouTube, offering both `single` and `batch processing` capabilities.

## Objective
The objective of this project is to provide an alternative python code for downloading YouTube content. Users can choose to download only the audio, or both audio and video, with options for specific video resolutions and batch processing of multiple URLs. 

## Output:

**Audio Only:** Downloads YouTube videos as MP3 files.

**Audio and Video:** Downloads YouTube videos as .webm files, merging the highest available quality audio and selected video resolution.

## Benefit to User:
This script is an alternative to downloading the videos using the YouTube app.  It simplifies the process of saving YouTube content for offline access, and replay using other apps apart from YouTube.  

- Download music or podcasts as MP3s.

- Save videos for later viewing without an internet connection.

- Process multiple video links efficiently using a batch file.

## Privacy Note
> Author is not liable for any copyright infringement. Use the downloads for personal use only, not for commercial purposes.

## Caution
> YouTube always changes its metadata.  This script is provided as a guide.  It is the user's responsibility to re-configure the code if the metadata of videos changes.  For example, this script does not work for videos 3 years old or older.  You will have to use another package besides `pytubefix`.

## Background
> I developed this script due to scheduling issues.  While downloading using the Youtube app is the recommended method, sometimes there are internet outages. And it became more convenient to download the videos and delete them later to conserve memory. This python package called `pytubefix` is publicly available for streaming access.  The existing package called`ffmpeg` is for high-quality audio conversion and video/audio merging, ensuring reliable and flexible downloads.  

## Features
### User Input

##### Mode: Choose between 'batch' for multiple videos or 'single' for one video.

##### Choice: Select 'audio' to download only the audio (converted to MP3) or 'both' to download audio and video (merged into a .webm file).

##### Resolution (if 'both' is chosen): Specify the desired video resolution (e.g., '1080p', '720p', '480p', '360p'). If the requested resolution is unavailable, the script defaults to the highest quality.

##### URL (if 'single' is chosen): Paste the YouTube video URL directly into the prompt.

## Instructions and Pre-work
This script assumes you can run python in the CLI or your favorite python IDE.  To use the batch processing feature, you have to create a file named list_of_addresses.txt in the same directory as the script. Each line in this file should contain a single YouTube video URL that you want to process.  Carefully watch the logs in the Console to find out which links are not downloading due to incompatible metadata structure vs. the package requirements.  This is especially true for older videos. 


