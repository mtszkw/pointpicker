from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Annotator(ABC):
    def __init__(self, annotations_limit : int=None, window_timeout : int=0):
        self.init_figure()
        self.annotations_limit = annotations_limit or 10000
        self.window_timeout = window_timeout

    @abstractmethod
    def run(self, image : str):
        pass

    def init_figure(self):
        self._fig = plt.figure()
        self._ax = self._fig.add_subplot(111)
        self._fig.canvas.set_window_title('PointPicker')

    def update_title(self, title : str):
        self._ax.set_title(title, fontsize=10)
        plt.draw()