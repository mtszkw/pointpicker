from PIL import Image
import matplotlib.pyplot as plt

from .annotator import Annotator
from .zoom_factory import zoom_factory


class PointAnnotator(Annotator):
    def __init__(self, annotations_limit : int=None, window_timeout : int=0):
        self._num_annotations = 0
        super().__init__(annotations_limit, window_timeout)

    def run(self, img_absolute_path : str):
        image = Image.open(img_absolute_path)
        plt.imshow(image)
        f = zoom_factory(self._ax, base_scale=1.5) 
        cid = self._fig.canvas.mpl_connect('button_press_event', self)

        self.update_title(f'Left-click to select first point.')
        points = plt.ginput(self.annotations_limit, timeout=self.window_timeout)
        plt.show()

        return points

    def __call__(self, event):
        if event.button == 1: # Left
            self._num_annotations += 1
            self.update_title(f'Point has been selected (total: {self._num_annotations}). Right-click to undo.')
        elif event.button == 3: # Right
            self._num_annotations -= 1
            self.update_title(f'Removed previously selected point. Select another point.')
        elif event.button == 2:
            self.update_title(f'Finished point selection ({self._num_annotations} points). Close the window to proceed.')
