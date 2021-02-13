import urllib.request
import json
import os  # 到系統的環境變數那邊，添加API_KEY的環境變數，環境變數需要重新讀取
from settings import API_KEY

print(API_KEY)


def get_all_video_in_channel(channel_id):
    api_key = os.getenv('API_KEY')

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + \
        'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
            api_key, channel_id)

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
    return video_links


# video_list = get_all_video_in_channel('UC6SeKyYGmo9qjIb8ekPlncw')
# print(len(video_list))
