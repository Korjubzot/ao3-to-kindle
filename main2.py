# Import necessary libraries
import requests
from pathlib import Path
from bs4 import BeautifulSoup

# UI imports
import tkinter as tk
from tkinter import Entry, Button, Label

def scraper(fic_url, output_name):
    # Scrape the fic for text
    response = requests.get(fic_url)
    response.raise_for_status()
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    fics = soup.find_all("div", class_="userstuff")

    # Define output file path
    # Could this be simplified?
    output_dir = Path.home() / "Desktop"
    output_file = output_dir / (output_name + '.txt')

    # Write the text to a file
    with open(output_file, "w") as file:
        print("Writing to file...")
        for fic in fics:
            file.write(fic.text)

    # Print success message
    print(f"Scraping complete! {output_name} is now available at {output_file}.")

# Functions for TKinter UI
# Autofills the UI for ease of testing
def autofill_test():
    print("Autofilling...")
    url_label.delete(0, tk.END)
    output_label.delete(0, tk.END)
    url_label.insert(0, "https://archiveofourown.org/works/12345678")
    output_label.insert(0, "test_output")

def scrape_button_click():
    print("Scraping...")
    fic_url = url_label.get()
    output_name = output_label.get()
    scraper(fic_url, output_name)

# TKinter UI
window = tk.Tk()
window.title("AO3 Scraper")

url_label = Label(window, text="Enter the URL of the fic:")
url_label = Entry(window, width=50)
url_label.pack()

output_label = Label(window, text="Enter the name of the output file:")
output_label = Entry(window, width=50)
output_label.pack()

scrape_button = Button(window, text="Scrape Fic", command=scrape_button_click)
scrape_button.pack()

test_autofill_button = Button(window, text="Autofill Test (for bugfixing!)", command=autofill_test)
test_autofill_button.pack()

window.mainloop()