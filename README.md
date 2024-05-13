# ao3-to-kindle

A lightweight tool to pull fics from archive-of-our-own and push them to your Kindle e-reader

# Description

This Python-based tool allows you to easily download fanfictions from AO3, convert them to PDF format, and send them directly to your Kindle device. It provides a simple and efficient way to enjoy your favorite fics on your e-reader. Written for Lena because my girlfriend likes fanfiction _and_ her Kindle so much.

# To Do

[ ] Sanitize inputs
[ ] Convert HTML text to PDF output
[ ] Allow for output location selection
[ ] Improve GUI and user-friendliness
[ ] Add email-to-Kindle support
[ ] Package as an executable for ease of use
[ ] Improve scraping to allow user to pull multiple chapters at a time
[ ] Build a testing suite

# Installation

1. Clone repo to local

```bash
    git clone https://github.com/Korjubzot/ao3-to-kindle
```

2. Navigate to project directory

```bash
    cd ao3-to-kindle
```

3. Install the required packages using pip

```bash
   pip install -r requirements.txt
```

# Usage

1. Run the script. On Windows, use:

```bash
    python main.py
```

    On MacOS and Linux, use

```bash
    python3 main.py
```

2. Copy and paste the URL of the fic you want to download
3. Select the name of the output
4. Press "Scrape"
5. Enjoy!

# Requirements

- Python 3.6 or higher
- pip
- BeautifulSoup4
- urlLib3

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Disclaimer

This tool is intended for personal use only. Please respect the rights of the authors on AO3 and do not distribute the downloaded fics without their permission.
