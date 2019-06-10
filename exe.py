import argparse
from handler.encoder import Encoder

parser = argparse.ArgumentParser(description='がぞーかんじへんかん')
parser.add_argument('-i', '--image', help='変換する画像')
parser.add_argument('-f', '--fineness', help='処理の細かさ（デフォ横50文字）')
args = parser.parse_args()

enc = Encoder()
enc.upload(args.image)
img = enc.preprocess('resize_gray', aa_width=int(args.fineness))
cchar_art = enc.img_2_cchar(img)
print(cchar_art)