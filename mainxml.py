import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

file = r"C:\Users\iratk\OneDrive\Рабочий стол\basic-files\newsafr.xml"

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse(file, parser)

root = tree.getroot()
description_list = root.findall("channel/item/description")

all_words = []

for descr in description_list:
    all_words.extend(descr.text.split())

filtered_words = [word for word in all_words if len(word) > 6]

words_count = {}

for word in filtered_words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

top_10_words = sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:10]

for index in range(10, 0, -1):
    word, count = top_10_words[10 - index]
    print(f'{index}: {word} ({count})')

