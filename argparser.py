import argparse

parser = argparse.ArgumentParser(description='Download transcripts for youtube videos.')
parser.add_argument('video_id', type=str, help='id of the video')
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--language', type=str, default='de',
                   help='transcript language')
parser.add_argument('-o', '--output', type=str, default='output.txt',
                   help='file name to save the transcript')
parser.add_argument('-s', '--save_with_timestamps', type=bool, default=True,
                   help='transcript with timing')
parser.add_argument('-t', '--translate', type=str, default=None,
                   help='translation language')
group.add_argument('-g', '--get', action='store_true',
                   help='get language list for the video')

args = parser.parse_args()