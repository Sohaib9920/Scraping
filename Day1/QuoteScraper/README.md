# QuoteScraper

This is first web scraping project, which utilizes the `requests` module and other utility libraries to scrape quotes from the [QuotestoScrape](https://quotes.toscrape.com/) website. Moreover, you will learn about important modules like `re`, `csv`, `argparse`, `os` and `html`.

# Demo

https://github.com/Sohaib9920/Big_Data/assets/134132129/050a913b-9930-451b-9396-201a80c60e16

## Usage

To use this project, follow the instructions below:

### Scrape Quotes from the First Page

Run `requests_1.py` to scrape quotes from the first page and store them in the `quotes_1.txt` file located in the `output` folder. Note that the code in `requests_1.py` has been upgraded to `requests_2.py` for further functionality.

### Scrape Quotes from Multiple Pages

Run `requests_2.py` to scrape quotes from multiple pages. This script allows you to specify the number of pages to scrape and the desired output file name.

Example command:

```
python requests_2.py {number of pages to scrape e.g '10'} {csv file name e.g 'quotes_10.csv'}
```
