from yt_concate.pipeline.Steps.preflight import Preflight
from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.initialize_yt import InitializeYT
from yt_concate.pipeline.Steps.download_captions import DownLoadCaptions
from yt_concate.pipeline.Steps.read_caption import ReadCaption
from yt_concate.pipeline.Steps.search import Search
from yt_concate.pipeline.Steps.download_videos import DownLoadVideos
from yt_concate.pipeline.Steps.edit_videos import EditVideos
from yt_concate.pipeline.Steps.postflight import Postflight
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


# CHANNEL_ID = 'UCKgpamMlm872zkGDcBJHYDg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownLoadCaptions(),
        ReadCaption(),
        Search(),
        DownLoadVideos(),
        EditVideos(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
