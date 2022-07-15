import json
import getopt, sys
from yt_dlp import YoutubeDL

#Get full command line arguments
full_cmd_arguments = sys.argv

#Arguments list
arguments_list = full_cmd_arguments[1:]
short_options = "hl:v"
long_options = ["help", "link=", "output=", "verbose"]

try:
    arguments, values = getopt.getopt(arguments_list, short_options, long_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

def download_video(url: str, quality="mp4"):
    ydl_opts = {
            'format': f'{quality}/bestvideo/bestaudio'
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        all_info = json.dumps(ydl.sanitize_info(info))
        video_title = info.get("title")
        print(video_title)
        #download
        print(ydl.download(URL))

for current_argument, current_value in arguments:
    if current_argument in ("-h", "--help"):
        print("You need help okay")
    elif current_argument in ("-l", "--link"):
        URL = current_value
        print(f"you added a link {current_value}")
        download_video(URL)
    elif current_argument in ("-v", "verbose"):
        print("You want to see all things")
