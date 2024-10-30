import csv
from os import listdir
from os.path import isfile, join

from main.config import RESOURCE_PATH
from util.pattern import MultitonByFirstArg

class ResourceContainer(metaclass = MultitonByFirstArg):
    RESOURCE_PATH = None
    FILE_FORMAT = None

    def __init__(self, name = None) -> None:
        self.name = name

    def get_special_resource(self):

        files = self._get_files()
        items = self._get_special_resource(files)
        return items
        
    def _get_files(self) -> list:
        if self.name is None:
            files = [join(self.RESOURCE_PATH, file_name) for file_name in listdir(self.RESOURCE_PATH) if isfile(join(self.RESOURCE_PATH, file_name)) and file_name.endswith(self.FILE_FORMAT)]
        else:
            full_name = self.name + self.FILE_FORMAT
            files = [join(self.RESOURCE_PATH, file_name) for file_name in listdir(self.RESOURCE_PATH) if isfile(join(self.RESOURCE_PATH, file_name)) and file_name == full_name]

        return files

    def _get_special_resource(self, files):
        items = list()

        for file_path in files:
            with open(file_path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                for line in csv_reader:
                    line = list(map(lambda string_data: string_data.strip(), line))
                    items.append(line)

        return items
    
class StickerContainer(ResourceContainer): 
    RESOURCE_PATH = join(RESOURCE_PATH, 'stickers')
    FILE_FORMAT = '.csv'

    def get_stickers(self):
        data = self.get_special_resource()
        stickers_list = list(map(lambda sticker_data: sticker_data[0], data))
        return stickers_list
    
class VoiceContainer(ResourceContainer): 
    RESOURCE_PATH = join(RESOURCE_PATH, 'sound')
    FILE_FORMAT = '.csv'

    def get_voices(self):
        return self.get_special_resource()
