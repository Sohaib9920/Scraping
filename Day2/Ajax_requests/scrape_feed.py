# SCRAPING THE https://www.espncricinfo.com/ FOR LATEST FEEDS WHICH ARE DYNAMICALLY LOADED INTO PAGE USING AJAX (fetch)

import requests


def get_feeds_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        feeds_data = response.json()
        return feeds_data
    except requests.RequestException:
        print("No response from API or invalid request. Please check for new API url if it has been changed and make sure your internet is good")
        return None
    

def generate_html(feeds):
    html_output = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cricket Feeds</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <h1 class="my-5 text-center fw-bold">Latest Cricket Feeds</h1>
    """

    for feed in feeds:
        containers = feed["containers"]
        for container in containers:
            if container["type"] == "DEFAULT":
                feed_item = container["item"]
                if feed_item["type"] == "STORY":
                    feed_story = feed_item["story"]
                    title = feed_story["seoTitle"]
                    summary = feed_story["summary"]
                    feed_image = feed_story["image"]
                    image_url = "https://p.imgci.com" + feed_image["url"]
                    image_caption = feed_image["caption"]

                    html_output += f"""
                    <div class="card mb-4">
                        <div class="row g-0">
                            <div class="col-md-4">
                                <img src="{image_url}" alt="{title}" class="card-img img-fluid">
                            </div>
                            <div class="col-md-8 d-flex flex-column">
                                <div class="card-body">
                                    <h4 class="card-title">{title}</h4>
                                    <p class="card-text">{summary}</p>
                                </div>
                                <div class="card-footer">
                                    <small class="text-muted">{image_caption}</small>
                                </div>
                            </div>
                        </div>
                    </div>
                    """

    html_output += """
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return html_output


def save_html(html_output, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_output)
        print("Feeds are successfully scraped into", filename)


def main():
    # Use query parameters of page=1 and records=50 (which are maximum records of feeds) in url
    api_url = "https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=pk&lang=en&page=1&records=50"
    feeds_data = get_feeds_data(api_url)
    
    if feeds_data and "results" in feeds_data:
        feeds = feeds_data["results"]
        html_output = generate_html(feeds)
        save_html(html_output, "feeds.html")
    else:
        print("No feeds result found!")


if __name__ == "__main__":
    main()