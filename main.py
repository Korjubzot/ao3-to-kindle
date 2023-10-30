import requests
import os
from bs4 import BeautifulSoup
import tkinter as tk

def scraper(url, output_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        fics = soup.find_all("div", class_="userstuff")
        if not fics:
            raise Exception("Error: no data found. Did you copy the right link?")
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_file = os.path.join(desktop_path, output_name + '.txt')
        with open(output_file, "w") as file:
            for fic in fics:
                file.write(fic.text)
        print("Scraping complete!", output_name, "is now on your Desktop.")
    except requests.exceptions.RequestException as e:
        print("Error retrieving data: ", e)


url = input("Copy and paste a link from ao3 here: ")
output_name = input("What would you like the file to be called? ")

scraper(url, output_name)