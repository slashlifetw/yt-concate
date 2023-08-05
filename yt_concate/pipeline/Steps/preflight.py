from yt_concate.pipeline.Steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Prefilght !')
        utils.create_dir()
