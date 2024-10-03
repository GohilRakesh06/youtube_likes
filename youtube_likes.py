import requests
import sys

def get_video_metrics(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=statistics"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            views = data['items'][0]['statistics']['viewCount']
            likes = data['items'][0]['statistics']['likeCount']
            print(f"Video ID: {video_id} - Views: {views}, Likes: {likes}")
        else:
            print("Video not found.")
    else:
        print("Error retrieving video metrics:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python youtube_metrics.py <video_id> <api_key>")
    else:
        video_id = sys.argv[1]
        api_key = sys.argv[2]
        get_video_metrics(video_id, api_key)
