import requests
import os
from bs4 import BeautifulSoup

url = "https://archiveofourown.org/works/49442698"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

fics = soup.find_all("div", class_="userstuff")
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "output.txt")
with open(output_file, "w") as file:
    for fic in fics:
        file.write(fic.text)