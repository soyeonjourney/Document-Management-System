import csv
import os
from wordcloud import WordCloud


BASE_DIR = os.path.dirname(__file__)
STOPWORDS = set(map(str.strip, open(os.path.join(BASE_DIR, 'stopwords')).readlines()))

conference_list = [
    ['ICCV', 'CVPR'],
    ['CVPR'],
    ['ICCV', 'CVPR'],
    ['CVPR'],
    ['ICCV', 'CVPR'],
    ['CVPR'],
    ['ICCV', 'CVPR'],
    ['CVPR', 'WACV'],
    ['WACV'],
]

for year, conferences in zip(range(2013, 2022), conference_list):
    txt = ''

    for conference in conferences:
        path = ''.join(['../requests/', conference, str(year), '.csv'])
        with open(path, 'r', encoding='utf-8') as f:
            data = csv.reader(f)
            for row in data:
                txt = txt + row[1] + ' '

    wordcloud = WordCloud(
        mode='RGBA',
        background_color=None,
        width=1280,
        height=720,
        stopwords=STOPWORDS,
        colormap='Pastel1',
    )
    wcd = wordcloud.generate(txt)
    wcd.to_file('./pictures/WordCloud-' + str(year) + '.png')
