import codecs
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font_file = 'TakaoPMincho.ttf'

ch_list = []
f = codecs.open('unicode.txt', 'r', 'utf-8')
count = 0
for row in f:
    if row[-1] == "\n": row = row[:-1]
    ch_list.append(row)
    count += 1
all_pix_data = []
font_size = 12
img_size = (font_size, font_size)
font = ImageFont.truetype(font_file, font_size, encoding='utf-8')
img = Image.new('RGB', img_size, (0,0,0))
draw = ImageDraw.Draw(img)
img_w, img_h = img_size
all_pix_num = 0
for ch in ch_list:
    draw.rectangle([0, 0, img_w, img_h], fill=(0,0,0))
    draw.text((0, 0), ch, fill=(255,255,255), font=font)
    col_count = 0
    for y in range(img_h):
        for x in range(img_w):
            c = img.getpixel((x,y))
            col_count += c[0]
            col_count += c[1]
            col_count += c[2]
    pix_data = {'uni':ch, 'num':col_count}
    print(pix_data)
    all_pix_data.append(pix_data)
    all_pix_num += col_count
print(all_pix_data)
all_pix_data.sort(key=lambda x: x['num'])
for pix_data in all_pix_data:
    print(pix_data["uni"],pix_data)
print("min:",all_pix_data[0],"max",all_pix_data[-1])
max_pix_num = all_pix_data[-1]['num']
str = ""
div_num = 256
pix_step = float(max_pix_num)/div_num
idx_step = float(len(all_pix_data)-1)/div_num
n = 0
now_pix_num = 0
idx = 0
no = 0
print("all_pix_num:",all_pix_num,"len:",len(all_pix_data), "pix_step:",pix_step,"idx_step:",idx_step)
for i in range(div_num):
    while(i*pix_step > all_pix_data[idx]["num"]):
        idx += 1
        if idx >= (i+1)*idx_step:
            idx -= 1
            break
    print("no:",no, "idx:",idx,"limit:",i*(idx_step+1),"uni:",all_pix_data[idx]["uni"], all_pix_data[idx]["num"])
    no += 1
    str += '%s\n' % all_pix_data[idx]["uni"]
    idx += 1
print(str)
with open('cchar_dic.umeume', 'w') as f:
    f.write(str)
print('completed!')