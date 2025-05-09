import bs4
import requests

#Make the HTTP Request
response = requests.get("https://en.wikipedia.org/wiki/Mathematics")

#Parse the HTML
if response is not None:
    html = bs4.BeautifulSoup(response.text, 'html.parser')

#Extract Page Title and Paragraphs
title = html.select("#firstHeading")[0].text
paragraphs = html.select("p")
for para in paragraphs:
    print(para.text)