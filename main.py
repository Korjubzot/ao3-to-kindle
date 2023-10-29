import requests
import os
from bs4 import BeautifulSoup

def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    fics = soup.find_all("div", class_="userstuff")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "output.txt")
    with open(output_file, "w") as file:
        for fic in fics:
            file.write(fic.text)

# url = user input (later)
url = input("Copy and paste a link from ao3 here:")


scraper(url)