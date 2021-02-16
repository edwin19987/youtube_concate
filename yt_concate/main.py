
from pipline.pipline import Pipline
from pipline.steps.get_video_list import GetVideoList
from pipline.steps.initialize_yt import InitializeYT
from pipline.steps.download_captions import DownloadCaptions
from pipline.steps.read_caption import ReadCaption
from pipline.steps.preflight import Preflight
from pipline.steps.postflight import Postflight
from pipline.steps.search import Search
from pipline.steps.download_video import DownloadVideos
from utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():  # pipline pattern
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible', 
    }

    steps = [  # 要執行的class
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]
    utils = Utils()

    p = Pipline(steps)
    p.run(inputs,utils)


if __name__ == '__main__':
    main()
