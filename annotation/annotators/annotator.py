from abc import ABC, abstractmethod

class Annotator(ABC):
    def __init__(self, annotations_limit=None, window_timeout=0):
        self.annotations_limit = annotations_limit or 10000
        self.window_timeout = window_timeout

    @abstractmethod
    def run(self, image):
        pass