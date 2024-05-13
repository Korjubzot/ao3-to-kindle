import requests
import os
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import Entry, Button, Label
from tkinter.ttk import Progressbar

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
        result_label.config(text=f"Scraping complete! {output_name} is now on your Desktop.")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error retrieving data: {e}. Please make sure you are only using a link to ao3")
    except Exception as e:
        result_label.config(text=str(e))

def scrape_button_click():
    url = url_entry.get()
    output_name = output_name_entry.get()
    if not url.startswith("https://archiveofourown.org"):
        result_label.config(text="Error: please enter a valid URL from ao3")
    elif not output_name:
        result_label.config(text="Error: please enter a file name")
    else:
        scraper(url, output_name)

window = tk.Tk()
window.title("AO3 Scraper")

url_label = Label(window, text="Copy and paste a link from ao3:")
url_label.pack()
url_entry = Entry(window, width=50)
url_entry.pack()

output_name_label = Label(window, text="What would you like the file to be called?")
output_name_label.pack()
output_name_entry = Entry(window, width=50)
output_name_entry.pack()

scrape_button = Button(window, text="Scrape", command=scrape_button_click)
scrape_button.pack()

result_label = Label(window, text="")
result_label.pack()

progress_bar = Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

window.mainloop()

# todo
# fix the progress bar
# validate filename input
# push to pdf format