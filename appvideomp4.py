import os
import yt_dlp

def download_video(url):
    # Define the options for yt-dlp
    opciones = {
        'format': 'bestvideo+bestaudio/best',  # Mejor video + mejor audio
        'outtmpl': '%(title)s.%(ext)s',       # Nombre del archivo
        'noplaylist': True,                    # No descargar listas de reproducción automáticamente
    }

    # Create a YoutubeDL instance with the defined options
    with yt_dlp.YoutubeDL(opciones) as ydl:
        try:
            # Download the video
            ydl.download([url])
            print(f"Download completed for: {url}")
        except Exception as e:
            print(f"Skipping unavailable video: {url}\nReason: {str(e)}")

def main():
    # List of URLs to download
    urls = [
        "https://m.ok.ru/video/3280067889804",
    ]

    # Download each URL
    for url in urls:
        download_video(url)

if __name__ == "__main__":
    main()
