# YouTube Video Search Automation with Selenium

This project automates the process of searching for a video on YouTube using Selenium WebDriver. In this example, the script navigates to YouTube, searches for "Baby Shark", and plays the first video in the search results.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (This will be automatically installed using `webdriver-manager`)
- Required Python libraries

## Installation

1. Clone this repository or copy the script.

2. Install the required Python libraries:

    ```bash
    pip install selenium webdriver-manager
    ```

3. Ensure you have Google Chrome installed.

## Running the Script

Once the prerequisites are installed, you can run the script to automate YouTube search:

1. Open a terminal or command prompt.
2. Run the Python script:

    ```bash
    python youtube_search.py
    ```

## How it Works

- The script uses Selenium WebDriver to control a Chrome browser instance.
- It opens YouTube and searches for "Baby Shark".
- It clicks on the first video that appears in the search results.

### Code Breakdown:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
option = Options()
option.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

# Navigate to YouTube
driver.get("https://www.youtube.com/")
driver.maximize_window()

# Allow the page to load
time.sleep(2)

# Locate the search bar
search_box = driver.find_element(By.NAME, "search_query")

# Enter "Baby Shark" into the search bar
search_box.send_keys("Baby Shark")

# Submit the search query (by pressing Enter)
search_box.send_keys(Keys.RETURN)

# Allow the search results to load
time.sleep(3)

# Click on the first video in the search results
first_video = driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
first_video.click()
