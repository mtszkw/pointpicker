from PIL import Image
import matplotlib.pyplot as plt

from .annotator import Annotator


class BoxAnnotator(Annotator):
    def __init__(self, annotations_limit=None, window_timeout=0):
        super().__init__(annotations_limit, window_timeout)

    def run(self, img_absolute_path : str):
        raise NotImplementedError("BoxAnnotator is not yet implemented")
