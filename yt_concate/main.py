
from pipline.pipline import Pipline
from pipline.steps.get_video_list import GetVideoList
from pipline.steps.download_captions import DownloadCaptions
from pipline.steps.read_caption import ReadCaption
from pipline.steps.preflight import Preflight
from pipline.steps.postflight import Postflight
from utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():  # pipline pattern
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [  # 要執行的class
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption(),
        Postflight()
    ]
    utils = Utils()

    p = Pipline(steps)
    p.run(inputs,utils)


if __name__ == '__main__':
    main()
