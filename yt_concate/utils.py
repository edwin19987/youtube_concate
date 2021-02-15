import os
from pipline.steps.settings import CAPTIONS_DIR
from pipline.steps.settings import DOWNLOADS_DIR
from pipline.steps.settings import VIDEOS_DIR
from pipline.steps.settings import VIDEO_LIST_FILENAME

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url)+'.txt')

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # 如果資料夾存在是OK的
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def caption_file_exist(self, url):  # 檢查文字檔案存不存在，避免一值重複跑
        path = self.get_caption_filepath(url)
        return  os.path.exists(path) and os.path.getsize(path) > 0  # 避免之前為下載到

    def get_video_list_filepath(self,channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id+'.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path)>0