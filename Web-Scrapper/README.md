# Simple Web Scraper
![a Web scrap](https://github.com/ashutosh786palhare/Python-Micro-Projects/assets/53346137/0626a353-3a75-4959-8742-d180d0531bbd)

This is a simple web scraping script written in Python that extracts email addresses and phone numbers from a webpage and crawls links found on that page up to a specified depth.

## Usage

**Clone the Repository**

   ```bash
   git clone https://github.com/your-username/simple-web-scraper.git
   ```
   
## Install Dependencies

Ensure you have Python installed. Install the required packages:

```bash
pip install beautifulsoup4
```

## Run the Script

Run the Python script main.py

```bash
python main.py
```

## Input Required Information

1. Enter the URL of the webpage you want to scrape.
2. Input the number of pages you want to crawl.
3. Optionally, provide a filter argument for specific URLs.

## Output
The script will scrape the webpage, extract email addresses and phone numbers, and display the collected data.

## Requirements
1. Python 3.x
2. BeautifulSoup (bs4) library


## Script Details
1. The script uses urllib.request to fetch web pages and BeautifulSoup for HTML parsing.
2. It extracts email addresses and phone numbers using regular expressions from the page content.
3. The depth of crawling links is determined by the number of pages specified.
4. The script allows an optional filter argument for specific URLs to crawl.

## Legal Considerations
Ensure that you have permission to scrape data from the website as per its terms of service or legal restrictions. Respect the website's policies when using this script.

## Disclaimer
This script is provided as-is, and its use is at your own risk. The authors are not liable for any misuse or legal consequences arising from the use of this script.
