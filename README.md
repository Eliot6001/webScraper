# Reddit Scraper

## Description

This Python script uses Selenium to scrape data from a Reddit subreddit and write the results into a text file of (Title, upvotes, links) format.

## Prerequisites

- Python 3
- Selenium
- ChromeDriver (ensure it's in the system PATH or provide the path to it in the script)
https://googlechromelabs.github.io/chrome-for-testing/

## Installation

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Install Pip
3. pip install -r requirements.txt (It's preferable if you run it in a virutal env)

## Usage

1. Run the script: `python reddit_scraper.py`.
2. Enter the subreddit when prompted.
3. The script will scrape data from the subreddit, and you will be prompted if you want to proceed to the next page.
4. The results will be written into a text file named according to the current date and time.

## Configuration

- ChromeDriver executable path is set in the `service = Service(executable_path="chromedriver.exe")` line. Make sure to provide the correct path to your ChromeDriver executable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
