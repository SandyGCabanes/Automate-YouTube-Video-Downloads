# sandy.g.cabanes
# Update: March 27, 2025
# Title: pytubefix_2025_batch_or_single.py
# Description
""" main: input audio only or both, resolution (try 360p or 480p first)
        and batch or single (batch option will look for a
        list_of_addresses.txt file in same folder)
    if batch: urls converted to list, process_video loop through list
    if single:
    wait_for_file helper function: Checks complete download of video file
        before staring the ffmeg merge
    process_video function: input url first (no need if batch)
        if audio: audio.download
        if both: audio.download and video.download then merge
"""

# -----------------------------------------------------------------------------
import os
import time
import subprocess
import ffmpeg
from pytubefix import YouTube
from pytubefix.cli import on_progress


# Helper function to wait for file to complete downloading
def wait_for_file(filename):
    """Pause execution until the specified file exists."""
    while not os.path.exists(filename):
        time.sleep(1)  # Wait for 1 second
    print(f"{filename} is ready for processing!")

# Process video function
def process_video(url, choice, input_resolution):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        if choice == "audio":
            # Download only audio
            audio = yt.streams.filter(only_audio=True).first()
            if audio:
                print(f'Downloading Audio for {yt.title}...')
                audio_file = f'{yt.title}_audio.mp4'
                audio.download(filename=audio_file)
                wait_for_file(f"{yt.title}_audio.mp4")  # Ensure download is complete

                # Convert MP4 to MP3 using ffmpeg
                output_audio = f"{yt.title}_audio.mp3"
                conversion_command = ["ffmpeg", "-y", "-i", audio_file, output_audio]
                conversion_result = subprocess.run(conversion_command)

                if conversion_result.returncode == 0:
                    print(f"Audio downloaded and converted to MP3: {output_audio}")
                else:
                    print("Error: Audio conversion to MP3 failed.")

                os.remove(audio_file)  # Delete temporary MP4 file

            else:
                print(f"Audio stream not available for {url}")

        elif choice == "both":
            # Download video
            video = yt.streams.filter(resolution=input_resolution).first()
            video_file = f'{yt.title}_video.mp4'
            if video:
                print(f'Downloading Video for {yt.title}...')
                video.download(filename=video_file)
                wait_for_file(f"{yt.title}_video.mp4")  # Ensure video download is complete
            else:
                print(f"Video stream not available for resolution {input_resolution}")

            # Download audio
            audio = yt.streams.filter(only_audio=True).first()
            audio_file = f'{yt.title}_audio.mp4'
            if audio:
                print(f'Downloading Audio for {yt.title}...')
                audio.download(filename=audio_file)
                wait_for_file(f"{yt.title}_audio.mp4")  # Ensure audio download is complete
            else:
                print(f"Audio stream not available for {url}")

            # Merge audio and video using ffmpeg
            if os.path.exists(video_file) and os.path.exists(audio_file):
                print(f"Merging audio and video for {yt.title}...")
                output_file = f"{yt.title}_merged.webm"
                ffmpeg.concat(ffmpeg.input(video_file), ffmpeg.input(audio_file), v=1, a=1).output(output_file).run()
                print(f"Merged file created: {output_file}")

                # Cleanup
                os.remove(video_file)
                os.remove(audio_file)
                print("Temporary files deleted.")
            else:
                print(f"Skipping merge for {yt.title} due to missing files.")

        else:
            print("Invalid choice. Please type 'audio' or 'both'.")
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

# Main script with inputs and batch or single --------------------------------
mode = str(input("Type 'batch' to process multiple videos or 'single' for one video -> ").lower())
choice = str(input("Type 'audio' for audio only or 'both' for audio and video -> ").lower())
input_resolution = str(input("Type resolution (1080p, 720p, 480p, 360p) -> "))

if mode == "batch": # Update list_of_addresses.txt
    print("Looking for list_of_addresses.txt in the current folder...")
    if os.path.exists("list_of_addresses.txt"):
        with open("list_of_addresses.txt", "r") as file:
            urls = [line.strip() for line in file if line.strip()]  # Clean and read each line

        for url in urls:
            print(f"Processing URL: {url}")
            process_video(url, choice, input_resolution)

        print("Batch processing completed.")
    else:
        print("Error: list_of_addresses.txt not found in the current folder.")

elif mode == "single":
    url = str(input("Paste URL here -> "))
    process_video(url, choice, input_resolution)
else:
    print("Invalid mode. Please type 'batch' or 'single'.")
