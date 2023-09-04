import sys

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
            yt_obj = YouTube(url=url, on_progress_callback=progress_function).streams.filter(
                progressive=True).get_highest_resolution()
            yt_obj.download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
            print()
        return data


def progress_function(s, chunk, bytes_remaining):
    total_size = s.filesize
    downloaded_size = total_size - bytes_remaining
    current = (downloaded_size / total_size)
    percent = '{0:.1f}'.format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(f'\r ↳ |{status}| {percent}% ({downloaded_size} bytes /{total_size} bytes)')
    sys.stdout.flush()
    # reference : https://github.com/pytube/pytube/issues/862
