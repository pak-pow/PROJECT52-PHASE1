# Week 6: Web Scraper Collection

**Category:** Backend / Automation | **Status:** Completed

## About

Web scraping is one of the most immediately practical Python skills. This project is not a single scraper but a collection of progressively more complex scripts, each targeting a different scraping challenge. Starting from a basic HTML parser and ending with a headless browser bot, this week covers the full range of modern web scraping techniques.

Each script is standalone and targets a specific type of site or problem. Output data is saved to CSV files in the same directory, making results immediately inspectable.

## What It Does

A collection of Python web scraping scripts demonstrating different tools and techniques: basic HTML parsing, multi-page pagination, structured data extraction, headless browser automation, and login bots.

## Learning Objectives

- Parsing HTML with `BeautifulSoup` to extract structured data
- Handling pagination to scrape data across multiple pages
- Storing scraped data cleanly in CSV format
- Using `Selenium` for JavaScript-heavy sites that require browser rendering
- Automating login flows with a headless browser bot

## Project Structure

```
week6_web_scrapper/
├── scrapper.py                 # Basic BeautifulSoup scraper
├── book_scrapper.py            # Scrapes book data with pagination
├── pagination_scrapper.py      # General-purpose pagination handler
├── selenium_scraper.py         # Selenium-based scraper for JS-rendered pages
├── headless_job_bot.py         # Headless browser job listing scraper
├── login_bot.py                # Automated login flow bot
├── books_inventory.csv         # Output: book inventory data
├── complete_library.csv        # Output: full library dataset (61KB)
├── hackernews.csv              # Output: Hacker News data
└── job_hunt.csv                # Output: Job listings data
```

## Tech Stack

- **Language:** Python 3
- **Libraries:** requests, BeautifulSoup4, Selenium
- **Output:** CSV files
