import urllib3
import bs4

from json import dump
from const import HEADERS, KEY_WORDS


def crawl(key_word):
    p = 0
    out_dict_list = []
    while True:
        p += 1
        url = f'https://burst.shopify.com/photos/search?page={p}&q={key_word}'
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        if response.status == 404:
            break
        else:
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            for img_title in soup.find_all('div', {'class': 'photo-tile'}):
                img_tag = img_title.find('img')
                out_dict_list.append({'image': img_tag['src'].split('?')[0],
                                      'host': 'Burst',
                                      'original': url,
                                      'title': key_word})

    return out_dict_list


if __name__ == '__main__':
    data = []
    for kw in KEY_WORDS:
        data += crawl(kw)

    with open('burst.json', 'w') as f:
        dump(data, f)
