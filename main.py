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
