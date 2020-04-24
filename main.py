from youtube_transcript_api import YouTubeTranscriptApi
from util import seconds_to_h_m_s_ms
from argparser import args

video_id = args.video_id
transcript_language = [args.language]
save_file_name = args.output
save_with_timestamps = args.save_with_timestamps
translation_language = args.translate
get_list = args.get

language_list = YouTubeTranscriptApi.list_transcripts(video_id)

if get_list:
    print(language_list)
    exit()


def get_translation(transcript, file_name, lang=None):
    if lang is not None:
        file_name = lang + "-" + file_name
    f = open(file_name, "w")
    for item in transcript:
        if not save_with_timestamps:
            f.write(item['text'] + "\n")
        else:
            start_time = item['start']
            f.write(seconds_to_h_m_s_ms(start_time) + " -> " + item['text'].replace('\n', '') + "\n")
    f.close()


transcript = None

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, transcript_language)
except Exception as e:
    print(e)


if transcript is not None:
    get_translation(transcript, save_file_name)
    if translation_language is not None:
        translated_transcript = language_list.\
            find_transcript(transcript_language).\
            translate(translation_language).\
            fetch()
        get_translation(translated_transcript, save_file_name, translation_language)
