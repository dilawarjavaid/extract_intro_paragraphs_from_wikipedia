# Wikipedia Intro Scraper

A beginner-friendly Python script that uses `requests` and `BeautifulSoup` to scrape the introductory paragraphs of a Wikipedia page and save them to a text file.

## Features

- Fetches the title and first few paragraphs of a Wikipedia article
- Extracts only the introductory content before the table of contents
- Saves the cleaned text to a local file named `intro.txt`

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies using:

```bash
pip install requests beautifulsoup4
````

## Usage

1. Make sure the script points to a Wikipedia URL:

   ```python
   response = requests.get("https://en.wikipedia.org/wiki/Mathematics")
   ```

2. Run the script:

   ```bash
   python scrape_intro.py
   ```

3. After running, check the generated `intro.txt` file for the extracted content.

## Output Example

The script will print the page title and introductory paragraphs, and save the first few paragraphs to:

```
intro.txt
```

## Customization

To scrape a different Wikipedia page, change the URL in the script:

```python
response = requests.get("https://en.wikipedia.org/wiki/Your_Topic_Here")
```

