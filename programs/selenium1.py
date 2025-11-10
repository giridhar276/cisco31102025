

from selenium import webdriver
import time

# Create Chrome browser
driver = webdriver.Chrome()

try:
    # Open Amazon home page
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    # Wait for a few seconds just to see the browser
    time.sleep(3)

    # Print page title and current URL
    print("Page title:", driver.title)
    print("Current URL:", driver.current_url)

finally:
    # Close the browser
    driver.quit()
