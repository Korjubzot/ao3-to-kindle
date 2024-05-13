# Import necessary libraries
import requests
from pathlib import Path
from bs4 import BeautifulSoup

# UI imports
import tkinter as tk
from tkinter import Entry, Button, Label, messagebox

# PDF handling imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Main scraper function
def scraper(fic_url, output_name):
    """Main scraper function
    Accepts a URL(fic_url) and an output name(output_name) as arguments
    Scrapes the fic at fic_url and writes the text to a file"""

    try:
        # Scrape the fic for text
        response = requests.get(fic_url)
        response.raise_for_status()
    except:
        error_handler.config(text="Error: Invalid URL. Please use a valid AO3 link.")
    
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    fics = soup.find_all("div", class_="userstuff")

    # Define output file path
    # Could this be simplified?
    output_dir = Path.home() / "Desktop"
    output_file = output_dir / (output_name + '.txt')

    # Write the text to a file
    try:
        with open(output_file, "w") as file:
            print("Writing to file...")
            for fic in fics:
                file.write(fic.text)
    except IOError as e:
        print(f"Error writing to file: {e}")
        return

    # Convert text file to PDF
    text_to_pdf(output_file, output_name)

    # Delete the text file
    output_file.unlink()

    # Print success message
    print(f"Scraping complete! {output_name} is now available at {output_file}.")

# This function handles text conversion to PDF
# No, I don't understand reportlab. How could you tell?
def text_to_pdf(input_txt, output_name):
    """Converts a text file to a PDF
    Accepts a text file(input_txt) and an output name(output_name) as arguments
    Text file should come from the scraper function, output_name from user input"""
    print("Converting to PDF...")
    try:
        output_dir = Path.home() / "Desktop"
        pdf_output = output_dir / f"{output_name}.pdf"
        pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
        doc = SimpleDocTemplate(str(pdf_output), pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []
        with open(input_txt, "r") as file:
            for line in file:
                elements.append(Paragraph(line, styles["Normal"]))

        doc.build(elements)
    except Exception as e:
        print(f"Error converting to PDF: {e}")

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
url_label.pack()
url_label = Entry(window, width=50)
url_label.pack()

output_label = Label(window, text="Enter the name of the output file:")
output_label.pack()
output_label = Entry(window, width=50)
output_label.pack()

scrape_button = Button(window, text="Scrape Fic", command=scrape_button_click)
scrape_button.pack()

test_autofill_button = Button(window, text="Autofill Test (for bugfixing!)", command=autofill_test)
test_autofill_button.pack()

error_handler = Label(window, text="Errors will be displayed here.")
error_handler.pack()

window.mainloop()