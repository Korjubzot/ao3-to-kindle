import requests
from pathlib import Path
from bs4 import BeautifulSoup

# PDF handling imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# UI imports
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
        desktop_path = Path.home() / "Desktop"
        output_file = desktop_path / (output_name + '.txt')
        with open(output_file, "w") as file:
            for fic in fics:
                file.write(fic.text)
        pdf_output = desktop_path / (output_name + '.pdf')
        text_to_pdf(output_file, pdf_output)
        output_file.unlink()
        result_label.config(text=f"Scraping complete! {pdf_output} is now on your Desktop.")

    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error retrieving data: {e}. Please make sure you are only using a link to ao3")
    except Exception as e:
        result_label.config(text=str(e))

def text_to_pdf(input_file, output_file):
    input_file = str(input_file)
    output_file = str(output_file)
    pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    with open(input_file, "r") as file:
        for line in file:
            elements.append(Paragraph(line, styles["Normal"]))

    doc.build(elements)

def scrape_button_click():
    url = url_entry.get()
    output_name = output_name_entry.get()
    if not url.startswith("https://archiveofourown.org"):
        result_label.config(text="Error: please enter a valid URL from ao3")
    elif not output_name:
        result_label.config(text="Error: please enter a file name")
    else:
        scraper(url, output_name)

# for testing purposes
def test_autofill():
    url_entry.delete(0, tk.END)
    output_name_entry.delete(0, tk.END)
    url_entry.insert(0, "https://archiveofourown.org/works/12345678")
    output_name_entry.insert(0, "test")

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

test_autofill_button = Button(window, text="Autofill (Bugtesting only!)", command=test_autofill)
test_autofill_button.pack()

result_label = Label(window, text="")
result_label.pack()

progress_bar = Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

window.mainloop()

# todo
# fix the progress bar
# validate filename input
# push to pdf format