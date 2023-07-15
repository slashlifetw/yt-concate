import urllib.request
import json

from yt_concate.pipeline.Steps.step import Step
from yt_concate.setting import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs):
        channel_id = inputs['channel_id']
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
        print(len(video_links))
        return video_links
