import glob
import os.path

from pydub import AudioSegment


class FileRoutines:
    def __init__(self):
        pass

    @staticmethod
    def load_folder_of_mp3(path: str) -> list[AudioSegment]:
        path = path.removesuffix('/')
        path = path.removesuffix('\\')

        files = glob.glob(path + os.path.sep + '*.mp3')
        result = [AudioSegment.from_mp3(mp3) for mp3 in files]
        return result

    @staticmethod
    def export_mp3(mp3: AudioSegment, path: str):
        mp3.export(path, format="mp3")
