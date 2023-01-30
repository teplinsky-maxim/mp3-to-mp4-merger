from pydub import AudioSegment


class Merger:
    def __init__(self, songs: list[AudioSegment]):
        if len(songs) == 0:
            raise ValueError('Can not merge empty songs!')
        self._songs = songs

    def merge(self) -> AudioSegment:
        result = self._songs[0]

        for song in self._songs[1:]:
            result = result + song

        return result
