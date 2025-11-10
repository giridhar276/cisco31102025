#Take a screenshot of Amazon homepage
from selenium import webdriver
import time

driver = webdriver.Chrome()
filename = time.strftime("screenshot_%d_%b_%Y_%s.jpg")
try:
    driver.get("https://www.amazon.in/")
    time.sleep(5)  # wait for page to load fully

    # Save screenshot to current folder
    driver.save_screenshot(filename)
    print(f"Screenshot saved as: {filename}")
finally:
    driver.quit()
