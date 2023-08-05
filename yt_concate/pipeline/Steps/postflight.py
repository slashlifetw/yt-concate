from yt_concate.pipeline.Steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postfilght !')
