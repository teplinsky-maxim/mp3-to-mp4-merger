import argparse
import os

from core.file_routines import FileRoutines
from core.merger import Merger


def process(path_to_mp3: str, result_path: str):
    merged_song_name = 'temp.mp3'
    picture_name = 'pic.png'

    mp3s = FileRoutines.load_folder_of_mp3(path_to_mp3)
    merger = Merger(mp3s)
    merged_song = merger.merge()
    FileRoutines.export_mp3(merged_song, merged_song_name)

    # https://stackoverflow.com/questions/64375367/python-convert-mp3-to-mp4-with-static-image
    os.system(f'ffmpeg -loop 1 -framerate 1 -i "{picture_name}" -i "{merged_song_name}"'
              ' -map 0:v -map 1:a -r 10 -vf "scale=\'iw-mod(iw,2)\':\'ih-mod(ih,2)\',format=yuv420p"'
              f' -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M {result_path}')


def main():
    parser = argparse.ArgumentParser(description='Merge many mp3 to single mp4')
    parser.add_argument('-p', '--path_to_folder_with_mp3', type=str,
                        help='Where are your mp3 located. For example: ./songs/nice_music or C:\\songs\\nice_music', required=True)
    parser.add_argument('-r', '--result_path', type=str, default='mp3-to-mp4-result.mp4',
                        help='Path to store the result (with name of file)', required=False)
    args = parser.parse_args()

    process(args.path_to_folder_with_mp3, args.result_path)


if __name__ == '__main__':
    main()
