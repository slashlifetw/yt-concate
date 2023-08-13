import os


from yt_concate.setting import DOWNLOADS_DIR
from yt_concate.setting import VIDEOS_DIR
from yt_concate.setting import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exists(self, video_filepath):
        return os.path.exists(video_filepath) and os.path.getsize(video_filepath) > 0

    def caption_format_refactor(self, url_id_captions):
        captions_inf = []
        for caption in url_id_captions:
            caption_line = caption['text']
            caption_start_time = caption['start']
            caption_end_time = caption['start'] + caption['duration']
            caption_time_inf = f'{caption_start_time}-->{caption_end_time}'
            caption_inf_packages = [caption_time_inf, caption_line]
            for caption_inf_package in caption_inf_packages:
                captions_inf.append(f'{caption_inf_package}\n')
        return captions_inf
