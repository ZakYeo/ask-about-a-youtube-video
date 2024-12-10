import yt_dlp
import os
from openai import OpenAI, ChatCompletion



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

def query_chatgpt_with_transcription(client, transcription):
    """
    Maintains a continual conversation with ChatGPT using the transcription as initial context.

    Parameters:
        client (OpenAI): An OpenAI client instance.
        transcription (str): The transcription text to use as context.
    """
    messages = [
        {"role": "system", "content": "You are an AI assistant. The user will ask questions about the following video transcription."},
        {"role": "user", "content": f"Here is the transcription of the video:\n\n{transcription}\n\nPlease use this as context for answering questions."}
    ]

    print("\nYou can now ask questions about the video. Type 'exit' to quit.\n")
    while True:
        user_question = input("Your question: ").strip()
        if user_question.lower() == "exit":
            print("Exiting the Q&A session.")
            break

        messages.append({"role": "user", "content": user_question})

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=500
            )

            print(f"ChatGPT's answer: {response.choices[0].message.content}")

            messages.append({"role": "assistant", "content": response.choices[0].message.content})
        except Exception as e:
            print(f"An error occurred during the query: {e}")

if __name__ == "__main__":


    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    video_url = input("Enter the YouTube video URL: ").strip()
    downloaded_file = download_youtube_video(video_url)

    if downloaded_file:
        transcription = transcribe_audio_with_api(client, downloaded_file)
        if transcription:
            print("\nTranscription complete. Starting Q&A session...")
            query_chatgpt_with_transcription(client, transcription)
        else:
            print("Failed to transcribe the audio.")

