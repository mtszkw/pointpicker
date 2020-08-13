import os

class DirectoryReader:
    def __init__(self, images_dir):
        self.base_path = images_dir
        self.images_list = [os.path.join(self.base_path, f) for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

    def all(self):
        return self.images_list
    