import requests
from bs4 import BeautifulSoup

'''
TODO
Split URLs in txt file into list
Scrape Character Name from <div id="page-title">

'''

def get_link_list():
    try:
        with open('npc-urls.txt', 'r') as f:
            data = f.read()
            npc_links = data.split('\n')[:-2]
    except FileNotFoundError as e:
        raise SystemExit(f'##### Source File Not Found! #####\n{e}')
    print(npc_links)
    return npc_links

get_link_list()