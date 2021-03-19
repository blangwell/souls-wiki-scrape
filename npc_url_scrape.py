import requests
from bs4 import BeautifulSoup

WIKI_URL = 'http://darksouls.wikidot.com/npcs'

def get_npc_links():
    print(f'Making a GET request to {WIKI_URL}')
    try:
        npc_idx = requests.get(WIKI_URL)
        npc_idx.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(f'##### Error during GET request! #####\n{e}')
    soup = BeautifulSoup(npc_idx.text, 'lxml')
    try:
        td = soup.find('td')
        anchor_tags = td.find_all('a')
    except AttributeError as e:
        raise SystemExit(f'##### Error scaping anchor tags! #####\n{e}')
    return anchor_tags

def write_hrefs(tags):
    if len(tags) == 0:
        raise SystemExit('##### No anchor tags to parse! Exiting ##### ')
    print('Writing HREFs to npc-urls.txt')
    f = open('npc-urls.txt', 'w')
    f.write('### List of Dark Souls Wikidot NPC Page URLS ###')
    for tag in tags:
        href = tag.get('href')
        f.write(f'http://darksouls.wikidot.com{href}\n')
    f.close()

links = get_npc_links()
write_hrefs(links)