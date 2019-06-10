import codecs

ch_list = []
f = open('JIS0208.txt', 'r')
for row in f:
    if row[0] != '#':
        if len(row.split("\t")) >= 4 and row.split("\t")[3] == "# <CJK>\n":
            c = row.split("\t")[2]
            ch_list.append(chr(int(c, 16)))
f.close()

f = codecs.open('unicode.txt', 'w', 'utf-8')
#txt = "".join(ch_list)
txt = "\n".join(ch_list)
f.write(txt)
f.close()