import requests
from bs4 import BeautifulSoup

WIKI_URL = 'http://darksouls.wikidot.com/npcs'

print('Sending a GET Request to Wikidot')
page = requests.get(WIKI_URL)
soup = BeautifulSoup(page.text, 'lxml')
td = soup.find('td')
links = td.find_all('a')

print('Writing HREFs to npc-urls.txt')
f = open('npc-urls.txt', 'w')
f.write('### List of Dark Souls Wikidot NPC Page URLS ###')
for link in links:
    href = link.get('href')
    f.write(f'http://darksouls.wikidot.com{href}\n')
f.close()