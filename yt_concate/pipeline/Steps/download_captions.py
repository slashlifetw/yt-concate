import time

from youtube_transcript_api import YouTubeTranscriptApi

from yt_concate.pipeline.Steps.step import Step


class DownLoadCaptions(Step):
    def process(self, data, inputs, utils):
        start_time = time.time()
        total_video_counts = 0
        available_video_counts = 0
        for yt in data:
            total_video_counts += 1
            print(f'checking whether the caption exists for {yt.url}')
            if utils.caption_file_exists(yt.caption_filepath):
                print('found existing caption file')
                continue
            try:
                captions = YouTubeTranscriptApi.get_transcript(yt.id)
                new_captions = utils.caption_format_refactor(captions)

                with open(yt.caption_filepath, 'w', encoding='utf-8') as f:
                    for caption_inf in new_captions:
                        f.write(caption_inf)
                print(f'downloading caption for {yt.url}')

            except Exception as e:
                error_message = [e]
                for take_error_message in error_message:
                    take_error_message = str(take_error_message)
                    if 'Subtitles are disabled' in take_error_message:
                        print(f'This Video({yt.id}) is not Captions !')
                    elif 'No transcripts were found for any of the requested language codes' in take_error_message:
                        print(f'This Video({yt.id}) has no English Captions !')
                    else:
                        print(e)
                continue

            available_video_counts += 1

        end_time = time.time()
        print(f'took {end_time - start_time} seconds')
        print(f'download {available_video_counts} captions / total {total_video_counts} captions')
        return data
