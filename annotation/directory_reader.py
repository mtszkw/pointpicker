import os

class DirectoryReaderIterator:
    def __init__(self, reader):
        self._index = 0
        self._reader = reader

    def __next__(self):
        if self._index >= len(self._reader._images_list):
            raise StopIteration
        
        self._index += 1
        return self._reader._images_list[self._index-1]
        

class DirectoryReader:
    def __init__(self, images_dir):
        self._base_path = images_dir
        self._images_list = self.__get_list(self._base_path)

    def __iter__(self):
        return DirectoryReaderIterator(self)

    def __get_list(self, path):
        images_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return list(map(lambda f: os.path.join(self._base_path, f), images_list))