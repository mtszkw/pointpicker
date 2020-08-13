from abc import ABC, abstractmethod

class Annotator(ABC):
    def __init__(self, annotations_limit : int=None, window_timeout : int=0):
        self.annotations_limit = annotations_limit or 10000
        self.window_timeout = window_timeout

    @abstractmethod
    def run(self, image : str):
        pass
