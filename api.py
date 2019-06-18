import json

import requests
from bs4 import BeautifulSoup
from flask import Flask

from scraper.scraper import Scraper

app = Flask(__name__)


@app.route('/<string:term>')
def get_result(term):
    # get links for 5 fiver results from Google
    result = Scraper.scrape_google(search_term=term)
    pages = []
    for l in result.split(" "):
        pages.append(l)

    required_tags = ["h1", "h2", "h3", "h4", "h5", "pre", "code", "p"]
    text_outputs = []
    code_outputs = []
    json_data = []
    for page in pages:
        res = requests.get(page)
        html_text = BeautifulSoup(res.text, 'html.parser')
        text = html_text.find_all(required_tags)
        for t in text:
            if t.name == 'code' or t.name == 'pre':
                code_outputs.append(t.get_text())
            else:
                text_outputs.append(t.get_text())

        data = {
            page: {
                "code_snippets": code_outputs,
                "relevant_text": text_outputs
            }
        }
        json_data.append(data)

    print(json_data)

    return json.dumps(json_data)


if __name__ == '__main__':
    app.run()
