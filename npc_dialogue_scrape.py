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

# GET npc page 
def get_npc_dialogue(npc_link):
    try:
        npc_page = requests.get(npc_link)
        npc_page.raise_for_status()
    except requests.exceptions.RequestException:
        raise SystemExit(f'##### Error during GET request #####')

    soup = BeautifulSoup(npc_page.text, 'lxml')
    for strong in soup('strong'):
        strong.decompose()
    for br in soup('br'):
        br.decompose()

    try: 
        # find dialogue container
        dialogue_container = soup.find('div', {'class': 'collapsible-block-content'})
        lis = dialogue_container.find_all('li')
    except AttributeError: 
        # if no dialogue, return an empty string
        return ''

    dialogue_arr = []
    dialogue = ''
    for li in lis:
        # remove bracketed annotations, newlines
        filtered_chunk = re.sub(r'\[.*\]|\n|\\', ' ', li.text)      
        if filtered_chunk != '' and filtered_chunk != ' ':
            dialogue += ' ' + filtered_chunk.strip()
            dialogue_arr.append(filtered_chunk.strip())
    print(dialogue_arr)
    time.sleep(5)


npc_links = get_link_list()
for link in npc_links:
    get_npc_dialogue(link)