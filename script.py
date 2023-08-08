import yt_dlp

def download_and_convert_to_wav(url, output_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_name}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Sample list of YouTube URLs
    youtube_urls = [
        "https://www.youtube.com/watch?v=dyF6wkV0P10"
    ]

    for idx, url in enumerate(youtube_urls, 1):
        download_and_convert_to_wav(url, f"output_{idx}")
