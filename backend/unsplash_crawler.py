import urllib3
import bs4

from json import dump
from const import HEADERS

KEY_WORDS = ['dog', 'cat', 'bunny', 'fox', 'tacos', 'kitten', 'wolf']
KEY_WORDS.sort()

def crawl(key_word):
    url = f'https://unsplash.com/s/photos/{key_word}?orientation=squarish'
    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.data, 'html.parser')

    out_dict_list = []
    for img_tag in soup.find_all('img'):
        if 'photo' in img_tag['src']:
            out_dict_list.append({'image': img_tag['src'],
                                  'host': 'Unsplash',
                                  'original': url,
                                  'title': key_word})

    return out_dict_list


if __name__ == '__main__':
    data = []
    for kw in KEY_WORDS:
        data += crawl(kw)

    with open('data.json', 'w') as f:
        dump(data, f)
