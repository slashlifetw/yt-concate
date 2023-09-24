from yt_concate.pipeline.Steps.step import Step

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(found.yt.video_filepath)
            if video.duration < end:
                continue
            cut_video = video.subclip(start, end)
            clips.append(cut_video)
            if len(clips) >= inputs['limit']:
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split('-->')
        return int(float(start)), int(float(end))
