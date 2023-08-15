# Scraping the single page from https://quotes.toscrape.com/#

import requests
import re
import html
import sys
import os


r = requests.get("https://quotes.toscrape.com/")
print(r.status_code)
html_content = r.text
quote_pattern = r'<span class="text" itemprop="text">(.*?)</span>'
author_pattern = r'<small class="author" itemprop="author">(.*?)</small>'

# . matches everything except newline. But our quote can expand across newline. So we will use `re.DOTALL` flag so that . also matches newline.

# ? makes the previous quantifier, which is *, non-greedy. It means that it matches as few characters as possible.
# This way </span> will be the end of first quote and not the last quote on page

# match group () is used so that findall only gives this group when pattern is matched. If there is no group then we will get complete pattern matches and
# if there are muliple groups then we get tuples of groups in matches.


quotes = re.findall(quote_pattern, html_content, re.DOTALL)  # findall gives list of matches and not object like finditer
authors = re.findall(author_pattern, html_content, re.DOTALL)


# sys.argv gives the list containing script name and all the command line arguments
if len(sys.argv) > 1:
    filename = sys.argv[1]  # Let user choose the txt filename
else:
    filename = "quotes_1.txt"  # Default filename is quotes_1.txt


# Create output directory if not exists already
output_directory = "output"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


with open(os.path.join(output_directory, filename), "w") as f:
    for quote, author in zip(quotes, authors):
        quote = html.unescape(quote)  # To convert html character references like &#39; to unicode
        author = html.unescape(author)
        f.write(f"Quote: {quote}\nAuthor: {author}\n\n")
    print(f"Check {filename} in {output_directory} directory")
