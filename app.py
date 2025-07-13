import os
import yt_dlp


def download_audio(url):
    # Define the options for yt-dlp
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }

    # Create a YoutubeDL instance with the defined options
    with yt_dlp.YoutubeDL(opciones) as ydl:
        try:
            # Download the audio
            ydl.download([url])
            print(f"Download and conversion completed for: {url}")
        except Exception as e:
            # Print error an message if something goes wrong
            print(f"Skipping unavailable video: {url}\nReason: {str(e)}")


def main():
    # List of URLs to download
    urls = [
        "https://www.youtube.com/playlist?list=PLshAoXpTEf3pjU8oe55vDAJ2oHxH2s9vX",
    ]

    # Download each URL
    for url in urls:
        download_audio(url)


if __name__ == "__main__":
    main()

