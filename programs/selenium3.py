
#Click on “Today’s Deals” link and print the heading


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome driver
driver = webdriver.Chrome()

try:
    # Maximize Chrome window
    driver.maximize_window()

    # Open Amazon India
    driver.get("https://www.amazon.in/")

    # Explicit wait
    wait = WebDriverWait(driver, 20)

    # Wait for the top navigation bar that holds links like:
    # Best Sellers, Mobiles, Today's Deals, Electronics, etc.
    nav_bar = wait.until(
        EC.presence_of_element_located((By.ID, "nav-xshop"))
    )

    # Get all <a> tags inside this navigation bar
    nav_links = nav_bar.find_elements(By.TAG_NAME, "a")

    print("Top navigation links:")
    count = 0
    for link in nav_links:
        text = link.text.strip()
        if text:
            count += 1
            print(f"{count}. {text}")

    if count == 0:
        print("No visible nav links found (UI might have changed).")

finally:
    driver.quit()
