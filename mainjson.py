# import os
# print("Текущая рабочая директория:", os.getcwd())

from pprint import pprint

import json

file = r"C:\Users\iratk\OneDrive\Рабочий стол\basic-files\newsafr.json"

with open(file, encoding='utf-8') as f:
    json_data = json.load(f)

news_list = json_data['rss']['channel']['items']
all_words = []

for row in news_list:
    all_words.extend(row['description'].split())

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






# Это код для тренировки записи
# with open(r"C:\Users\iratk\OneDrive\Рабочий стол\basic-files\result.json", 'w', encoding='utf-8') as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=2)


