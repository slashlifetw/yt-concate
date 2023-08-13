from pytube import YouTube

from yt_concate.pipeline.Steps.step import Step
from yt_concate.setting import VIDEOS_DIR


class DownLoadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print(f'videos to downloading={yt_set}')

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt.video_filepath):
                print(f'found existing video file for {url}, skipping')
                continue
            print('downloading', url)
            yt_obj = YouTube(url).streams.get_highest_resolution()
            yt_obj.download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
        return data
# create progressbar
