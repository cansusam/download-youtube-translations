import argparse

parser = argparse.ArgumentParser(description='Download transcripts for youtube videos.')
parser.add_argument('video_id', type=str, help='id of the video')
parser.add_argument('transcript_language', type=str, default='de',
                   help='transcript language')
parser.add_argument('-o', '--output', type=str, default='output.txt',
                   help='file name to save the transcript')
parser.add_argument('-s', '--save_with_timestamps', type=bool, default=True,
                   help='transcript with timing')
parser.add_argument('-t', '--translate', type=str, default=None,
                   help='translation language')
parser.add_argument('-l', '--list', action='store_true',
                   help='get language list for the video')

args = parser.parse_args()