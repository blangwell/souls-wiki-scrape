import re
import requests
import time
from bs4 import BeautifulSoup

# Split URLs in txt file into list
def get_link_list():
    try:
        with open('npc-urls.txt', 'r') as f:
            data = f.read()
            npc_links = data.split('\n')[:-2]
    except FileNotFoundError as e:
        raise SystemExit(f'##### Source File Not Found! #####\n{e}')
    return npc_links

def get_npc_dialogue(npc_links):
    try:
        npc_page = requests.get(npc_links[0])
        npc_page.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(f'##### Error during GET request #####')

    soup = BeautifulSoup(npc_page.text, 'lxml')

    try: 
        dialogue_container = soup.find('div', {'class': 'collapsible-block-content'})
    except AttributeError as e: 
        raise SystemExit(f'##### Error finding dialogue container #####')
    lis = dialogue_container.find_all('li')

    def extract_strong_tags(html):
        try:
            for li in html:
                unwanted = li.find('strong')
                unwanted.extract()
            extract_strong_tags(html)
        except AttributeError:
            pass
        finally:
            return html

    # recursively extract all strong tags from resultset
    destronged = extract_strong_tags(lis)
    dialogue = ''
    for li in destronged:
        filtered = re.sub('\[.*\]|\n+', ' ', li.text)
        if filtered != ' ':
            dialogue += filtered.strip()
    print(repr(dialogue))


npc_links = get_link_list()
get_npc_dialogue(npc_links)