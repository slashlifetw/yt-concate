import urllib.request
import json
from yt_concate.setting import API_KEY


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + f'key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        response = json.load(inp)

        for i in response['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = response['nextPageToken']
            url = first_url + f'&pageToken={next_page_token}'
        except KeyError:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
