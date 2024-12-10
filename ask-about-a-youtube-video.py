import yt_dlp
import os
from openai import OpenAI



def download_youtube_video(video_url):
    """
    Downloads a YouTube video as an .mp4 file to the current directory.

    Parameters:
        video_url (str): The URL of the YouTube video to download.
    """
    try:
        ydl_opts = {'outtmpl': '%(title)s.%(ext)s', 'format': 'mp4'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            print("Download complete!")
            return f"{info['title']}.mp4"
    except Exception as e:
        print(f"An error occurred during download: {e}")
        return None

def transcribe_audio_with_api(client, file_path):
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
                )
    return transcript

if __name__ == "__main__":


    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    video_url = input("Enter the YouTube video URL: ").strip()
    downloaded_file = download_youtube_video(video_url)

    if downloaded_file:
        print(transcribe_audio_with_api(client, downloaded_file))

