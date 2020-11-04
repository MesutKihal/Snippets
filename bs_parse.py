from bs4 import BeautifulSoup
import requests
import re

source = requests.get("https://www.lifewire.com/list-of-executable-file-extensions-2626061").text
soup = BeautifulSoup(source,'lxml')
arr = []
for article in  soup.find_all('tr'):
	arr.append(str(article.td)[4:-5])

for item in arr:
        if re.fullmatch(r'[A-Z][A-Z][A-Z]{1,2}', item) and item != ('RUN','PRG','OUT','KSH','IPA','CSH','ACTION'):
                print(item)
