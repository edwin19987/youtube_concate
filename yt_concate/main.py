from pipline.pipline import Pipline
from pipline.steps.get_video_list import GetVideoList

CHANNEL_ID = 'UC6SeKyYGmo9qjIb8ekPlncw'

def main():  #pipline pattern
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [  #要執行的class
        GetVideoList(),
    ]

    p = Pipline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
