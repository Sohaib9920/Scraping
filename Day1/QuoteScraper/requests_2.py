import requests
import re
import html
import csv
import argparse
import os


# Scrape quotes from the first ten pages of https://quotes.toscrape.com/#
def main():

    # Defining and extracting the command line arguments
    parser = argparse.ArgumentParser(description="Scrape quotes from 'https://quotes.toscrape.com/'")
    parser.add_argument('n', type=int, help='number of pages to scrape')
    parser.add_argument('f', type=str, help='output csv file name')
    args = parser.parse_args()
    # Use `python requests_2.py --help` in terminal to see usage

    # Running the scraper
    scrape_data = scrape_quotes(args.n)
    save_to_csv(args.f, scrape_data)


# Extract quotes from a single page
def extract_quotes_from_page(page_content):
    quote_pattern = r'<span class="text" itemprop="text">“(.*?)”</span>'  # Not including “ and ” in our match group
    author_pattern = r'<small class="author" itemprop="author">(.*?)</small>'

    quotes = re.findall(quote_pattern, page_content, re.DOTALL) 
    authors = re.findall(author_pattern, page_content, re.DOTALL)

    return quotes, authors


# Scrape quotes from multiple pages
def scrape_quotes(num_pages):
    all_quotes = []

    for page in range(1, num_pages+1):
        url = f'https://quotes.toscrape.com/page/{page}/'
        response = requests.get(url)
        if response.status_code == 200:
            quotes, authors = extract_quotes_from_page(response.text)
            all_quotes.extend(zip(quotes, authors))
            print(f"Scraped quotes from page {page}")
        else:
            print(f"Failed to retrieve page {page}")
        
    return all_quotes


# Write quotes to a csv file
def save_to_csv(filename, scrape_data):
    """
        scrape_data = List containing tuples of (quote, author) 
    """

    # Create output directory if not exists already
    output_directory = "output"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(os.path.join(output_directory, filename), 'w', newline='', encoding='utf-8-sig') as f:  
        # sig allows Excel to correctly identify the file's encoding.
        writer = csv.writer(f)
        writer.writerow(['Quote', 'Author'])  # Write header row

        for quote, author in scrape_data:
            quote = html.unescape(quote) 
            author = html.unescape(author)
            writer.writerow([quote, author])  # Write data row
    
    print(f"Scraped quotes written to {filename} in {output_directory} directory")


if __name__ == '__main__':
    main()    

