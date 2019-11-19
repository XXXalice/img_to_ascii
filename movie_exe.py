import argparse
from handler.movie_encoder import MovieEncoder

parser = argparse.ArgumentParser(description='どーがかんじへんかん')
parser.add_argument('-m', '--movie', help='変換する動画')
parser.add_argument('-f', '--fineness', help='処理の細かさ（デフォ横50文字）')
parser.add_argument('-fp', '--frame', help='処理するFPS（デフォ10f/s）')
parser.add_argument('-r', '--reverse', help='濃淡の反転')
args = parser.parse_args()
args.fineness = 50 if args.fineness is None else args.fineness
args.frame = 10 if args.frame is None else args.frame
args.reverse = True if args.reverse == 'true' else 0

enc = MovieEncoder(fps=args.frame)

#ここからテスト
# enc.show_movie(fpath=args.movie)

frames = enc.frame_capture(fpath=args.movie)
enc.log.debug(type(frames[0]))