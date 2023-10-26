import requests
from bs4 import BeautifulSoup

url = "https://archiveofourown.org/works/49442698"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

fics = soup.find_all("div", class_="userstuff")
with open("output.txt", "w") as file:
    for fic in fics:
        file.write(fic.text)