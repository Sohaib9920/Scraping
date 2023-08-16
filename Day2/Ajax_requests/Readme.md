# Project Description:

SCRAPING THE https://www.espncricinfo.com/ FOR LATEST FEEDS WHICH ARE DYNAMICALLY LOADED INTO PAGE USING AJAX (fetch). THE SCRAPED FEEDS DATA IS CONVERTED TO HTML.

## Setup:

- Open the homepage of cricinfo using https://www.espncricinfo.com/ 
- Open the network tab in developer options and filter type by 'Fetch/XHR'
- Scroll the page downward and try to find the fetch request which seems to be giving a JSON response of feeds data
- Copy the url for api_url
- Open this url on brwoser to see the json. Try to change the query parameters of page and records. 
- Copy the Json response and paste it into https://codebeautify.org/jsonviewer for neat json.
- IMPORTANT: Spend most of your time in understanding the staruture of json. Try to find how desired entries can be accessed most effectively
- After this, You are ready to use the api_url to get json and the parse it to html

# Ajax requests in webscraping

**What is AJAX:** AJAX (Asynchronous JavaScript and XML) is a technique that enables web applications to update specific content on a webpage without requiring a full page reload. 

**How it Works:** When a user interacts with a page, JavaScript sends an AJAX (XHR or fetch) request to the server. The server processes the request and returns data (often in JSON or XML format). The JavaScript then updates the webpage's content dynamically.

**Problem in Web Scraping:** The content from AJAX requests is appended to the webpage when specific events, such as scrolling, are detected by JavaScript on the client side. This poses a challenge for traditional web scrapers that focus on static page content and might miss dynamically loaded data.

**Solution:** To overcome this challenge, you can use API endpoints provided by websites. APIs offer direct access to data, including the content loaded through AJAX. By using APIs, you bypass the need to simulate AJAX requests, ensuring you retrieve all the desired information 