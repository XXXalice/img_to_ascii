import argparse
from handler.encoder import Encoder

parser = argparse.ArgumentParser(description='がぞーかんじへんかん')
parser.add_argument('-i', '--image', help='変換する画像')
parser.add_argument('-f', '--fineness', help='処理の細かさ（デフォ横50文字）')
parser.add_argument('-r', '--reverse', help='濃淡の暗転')
args = parser.parse_args()
args.fineness = 50 if args.fineness is None else args.fineness
args.reverse = True if args.reverse == 'true' else 0

enc = Encoder()
enc.upload(args.image)
img = enc.preprocess('resize', aa_width=int(args.fineness))
cchar_art = enc.img_2_cchar(img, reverse_mode=args.reverse)