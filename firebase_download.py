from firebase_admin import credentials, db
import yt_dlp
from dotenv import dotenv_values
config = dotenv_values(".env")
firebase_url = config['FIREBASE_DB']

# Initialize Firebase
cred = credentials.Certificate("path_to_your_firebase_admin_sdk_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase_url
})

# Reference to the queue in Firebase Realtime Database
ref = db.reference('queue')

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

def listener(event):
    # Check for new URLs and process them
    youtube_url = event.data
    if youtube_url:
        # Use your download function here
        download_and_convert_to_wav(youtube_url, "some_output_name")
        # Remove the URL from the queue if desired
        event.reference.delete()

# Listen for updates to the queue
ref.listen(listener)
