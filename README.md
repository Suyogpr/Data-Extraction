Web Scraper using Playwright (Ekantipur News & Cartoon Section)

This project is a browser automation script built using Python and Playwright to extract structured data from the Ekantipur website. It scrapes content from multiple sections including entertainment/news and cartoon pages, handling dynamic content loading, scrolling, and inconsistent HTML structures.
The goal of this project is to demonstrate web scraping skills, DOM traversal, data cleaning, and handling real-world messy web data.

Tech Stack
Python
Playwright (Browser Automation)
HTML/CSS Selectors (DOM parsing)

Features
Navigates multiple pages of a website
Handles dynamic content loading
Scrolls pages to trigger lazy-loaded content
Extracts structured data (title, author, image URL)
Handles missing or inconsistent data safely
Removes duplicate entries using a set
Returns clean structured Python dictionaries

How It Works
1. Page Navigation

The script uses Playwright to open web pages and navigate between sections like:

Entertainment
Cartoon

2. Waiting for Page Load

It ensures content is fully loaded using:

wait_for_selector()
wait_for_load_state("networkidle")
controlled time delays for stability

3. Scrolling for Dynamic Content

Some content loads only after scrolling. The script uses JavaScript execution:

Scrolls the page
Waits for new content to load

4. Data Extraction

The scraper collects:

Title
Author
Image URL

from structured HTML elements using CSS selectors.

5. Data Cleaning & Validation

To ensure data quality:

Skips empty or missing values
Removes duplicates using a set
Handles inconsistent formats (e.g., "Title - Author")

Challenges Handled
Dynamic page loading (lazy content)
Missing or inconsistent HTML structure
Duplicate entries in scraped data
Combined fields (title + author parsing)

How to Run
python scraper.py

Key Learnings
Browser automation using Playwright
DOM traversal using CSS selectors
Handling real-world messy web data
Data cleaning and deduplication techniques
Working with dynamic web pages