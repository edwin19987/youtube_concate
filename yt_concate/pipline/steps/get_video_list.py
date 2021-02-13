import urllib.request
import json
import os
from pipline.steps.step import Step, StepException
from pipline.steps.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs):
        api_key = os.getenv('API_KEY')

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + \
            'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
                API_KEY, inputs['channel_id'])

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:  # 因為到最後抓完沒有下一頁了
                break
        print(video_links)
        return video_links
