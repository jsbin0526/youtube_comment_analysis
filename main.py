import dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

if __name__ == "__main__":
    dotenv.load_dotenv()
    YOUTUBE_API_KEY = dotenv.get_key(dotenv.find_dotenv(), "YOUTUBE_API_KEY")
    if YOUTUBE_API_KEY:
        print(f"Loaded YouTube API Key: {YOUTUBE_API_KEY}")
    else:
        print("YouTube API Key not found in .env file.")
    YOUTUBE_API_SERVIE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVIE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

    # Example: Search for videos related to "Data Science"
    search_response = youtube.search().list(q="Data Science", order="relevance", part="snippet", maxResults=5).execute()
    for search_result in search_response.get("items", []):
        print(f"Title: {search_result['snippet']['title']}")
        print(f"Description: {search_result['snippet']['description']}\n")