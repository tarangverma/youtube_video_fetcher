import requests
from celery import shared_task
from .models import Video

API_KEYS = ["your_api_key", "your_api_key"]
SEARCH_QUERY = "official cricket"
POLL_INTERVAL = 10
current_api_key_index = 0

@shared_task
def fetch_videos_from_youtube():
    global current_api_key_index
    api_key = API_KEYS[current_api_key_index]
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": SEARCH_QUERY,
        "type": "video",
        "order": "date",
        "key": api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        for item in response.json().get("items", []):
            snippet = item.get("snippet", {})
            Video.objects.update_or_create(
                video_id=item["id"]["videoId"],
                defaults={
                    "title": snippet.get("title"),
                    "description": snippet.get("description"),
                    "published_at": snippet.get("publishedAt"),
                    "thumbnails": snippet.get("thumbnails"),
                },
            )
    elif response.status_code == 403:
        current_api_key_index = (current_api_key_index + 1) % len(API_KEYS)
