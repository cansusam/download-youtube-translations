from youtube_transcript_api import YouTubeTranscriptApi

import sys


def seconds_to_h_m_s_ms(seconds: float) -> str:
    int_seconds = int(seconds)
    ms = int(str(seconds).split('.')[1])
    s = int_seconds % 60
    m = int(s / 60)
    h = int(m / 60)

    return f"{h:02d}:{m:02d}:{s:02d}.{ms:02d}"


if len(sys.argv) < 3:
    print("There should be at least 2 arguments, video_id  translation_language [file_name] [time_stamp_true]")
    video_id = sys.argv[1]
    language_list = YouTubeTranscriptApi.list_transcripts(video_id)
    if len(language_list) > 0:
        print("Available languages for the given video:")
    for lang in language_list:
        print(lang)
    exit()

if len(sys.argv) >= 4:
    save_file_name = sys.argv[3]
else:
    save_file_name = 'output.txt'

if len(sys.argv) == 5:
    save_with_timestamps = sys.argv[4]
else:
    save_with_timestamps = True


video_id = sys.argv[1]
translation_language = [sys.argv[2]]

translation = YouTubeTranscriptApi.get_transcript(video_id, translation_language)

f = open(save_file_name, "w")

for item in translation:
    if not save_with_timestamps:
        f.write(item['text'] + "\n")
    else:
        start_time = item['start']

        f.write(seconds_to_h_m_s_ms(start_time) + " -> " + item['text'].replace('\n', '') + "\n")

f.close()
