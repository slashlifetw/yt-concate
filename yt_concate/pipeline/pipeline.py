from yt_concate.pipeline.Steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(date, inputs)
            except StepException as e:
                print('Exception happened:', e)
                break
