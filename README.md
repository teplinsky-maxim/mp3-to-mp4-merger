### .mp3 ➜ .mp4 merger ➕ 📼

---

🐍 Python3.10+

### Reason

Recently, I had a copyright issue with some music I uploaded on YouTube, and the video was blocked in certain countries. Since there is no other way to determine if YouTube will block the video, I wrote a script that allows you to merge your tracks into one and then convert it to MP4. You can then upload it to YouTube for checking without publishing to see if there are any copyright issues.


### Usage

```
usage: main.py [-h] -p PATH_TO_FOLDER_WITH_MP3 [-r RESULT_PATH]

Merge many mp3 to single mp4

options:
  -h, --help            show this help message and exit
  -p PATH_TO_FOLDER_WITH_MP3, --path_to_folder_with_mp3 PATH_TO_FOLDER_WITH_MP3
                        Where are your mp3 located. For example:
                        ./songs/nice_music or C:\songs\nice_music
  -r RESULT_PATH, --result_path RESULT_PATH
                        Path to store the result (with name of file)

Process finished with exit code 0
```