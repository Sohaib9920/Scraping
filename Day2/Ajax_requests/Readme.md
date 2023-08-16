# Project Description

This project involves scraping **[espncricinfo](https://www.espncricinfo.com/)** to collect the latest cricket feeds. These feeds are dynamically loaded onto the page using AJAX (fetch) requests. The scraped feed data is then transformed into HTML format.

## Setup

1. Visit the homepage of ESPNcricinfo by navigating to **[espncricinfo](https://www.espncricinfo.com/)**.
2. Open the developer options in your browser and go to the "Network" tab.
3. Filter the network requests by selecting the "Fetch/XHR" type.
4. Scroll down the page to trigger the loading of new content. Look for the fetch request that seems to provide a JSON response containing feeds data.
5. Copy the URL from this fetch request; this will be your `api_url`.
6. Paste the `api_url` into a browser to view the JSON response. Experiment with modifying query parameters like `page` and `records`.
7. For better readability, paste the JSON response into an online JSON viewer tool like **[codebeautify](https://codebeautify.org/jsonviewer)**.
8. **Important:** Spend ample time understanding the JSON structure. Determine the most efficient way to access desired information within the JSON data.
9. With a clear understanding of the JSON structure, proceed to use the `api_url` to fetch JSON data and convert it into HTML format.

# Ajax requests in webscraping

- **What is AJAX:**

  AJAX (Asynchronous JavaScript and XML) is a technique that enables web applications to update specific content on a webpage without requiring a full page reload. 

- **How it Works:**

  When a user interacts with a page, JavaScript sends an AJAX (XHR or fetch) request to the server. The server processes the request and returns data (often in JSON or XML  format). The JavaScript then updates the webpage's content dynamically.

- **Problem in Web Scraping:**

  The content from AJAX requests is appended to the webpage when specific events, such as scrolling, are detected by JavaScript on the client side. This poses a challenge for traditional web scrapers that focus on static page content and might miss dynamically loaded data.

- **Solution:** 

  To overcome this challenge, one simple solution might be to use API endpoints provided by websites. APIs offer direct access to data, including the content loaded through AJAX. By using APIs, you bypass the need to simulate AJAX requests, ensuring you retrieve all the desired information

# Usage
```bash
$ pip install requests
```
```bash
$ python scrape_feed.py
```
