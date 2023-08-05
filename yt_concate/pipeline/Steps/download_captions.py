import time

from youtube_transcript_api import YouTubeTranscriptApi

from yt_concate.pipeline.Steps.step import Step


class Downloadcaptions(Step):
    def process(self, data, inputs, utils):
        start_time = time.time()
        total_video_counts = 0
        available_video_counts = 0
        for url in data:
            total_video_counts += 1
            print(f'downloading caption for {url}')
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue
            try:
                url_id_captions = YouTubeTranscriptApi.get_transcript(utils.get_video_id_from_url(url))
            except Exception as e:
                error_message = [e]
                for take_error_message in error_message:
                    take_error_message = str(take_error_message)
                    if 'Subtitles are disabled' in take_error_message:
                        print(f'This Video({utils.get_video_id_from_url(url)}) is not Captions !')
                    elif 'No transcripts were found for any of the requested language codes' in take_error_message:
                        print(f'This Video({utils.get_video_id_from_url(url)}) has no English Captions !')
                    else:
                        print(e)
                continue

            with open(utils.get_caption_filepath(url), 'w', encoding='utf-8') as f:
                for _ in url_id_captions:
                    f.write(f'{_}\n')
            available_video_counts += 1

        end_time = time.time()
        print(f'took {end_time - start_time} seconds')
        print(f'download {available_video_counts} captions / total {total_video_counts} captions')
