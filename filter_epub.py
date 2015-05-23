import sys
from ebooklib import epub

if len(sys.argv) != 4:
    print 'Usage: main.py [filter file] [input epub file] [output epub file]'
    sys.exit()

filter_filename = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]

with open(filter_filename) as f:
    filter_words = f.read().splitlines()

book = epub.read_epub(input_filename)

for item in book.items:
    if isinstance(item, epub.EpubHtml):
        for word in filter_words:
            stars = '*' * len(word)
            item.content = item.content.replace(word, stars)

epub.write_epub(output_filename, book, {})
