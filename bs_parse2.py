from bs4 import BeautifulSoup
import requests
import re

source = requests.get("https://www.w3resource.com/python-exercises/python-basic-exercises.php").text
soup = BeautifulSoup(source,'lxml')
arr = []
for article in  soup.find_all('p'):
	arr.append(article.text)



with open('Python exercice.docx', 'a') as f:
        for item in arr:
                if item != '' and item[0].isdigit():
                        f.write(str('\n')+item)
                else:
                        f.write(item)
                        


