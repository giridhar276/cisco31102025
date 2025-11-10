

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# Demo credentials for SauceDemo
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Dummy checkout info
FIRST_NAME = "John"
LAST_NAME = "Doe"
ZIP_CODE = "500001"

# --- Configure Chrome ---
chrome_options = webdriver.ChromeOptions()

# Try to keep Chrome “clean” and reduce password popups
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
}
chrome_options.add_experimental_option("prefs", prefs)

# Optional: new “guest” profile so no saved passwords
chrome_options.add_argument("--guest")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Open site and maximize window
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 15)

    # 2. Login
    username_box = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    password_box = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_box.clear()
    username_box.send_keys(USERNAME)
    password_box.clear()
    password_box.send_keys(PASSWORD)
    login_button.click()

    # === CLOSE CHROME PASSWORD POPUP (if it appears) ===
    # Small pause to allow popup to show
    time.sleep(2)
    # Try pressing Enter and Esc – one of these usually dismisses it
    for key in ("enter", "esc"):
        pyautogui.press(key)
        time.sleep(0.5)
    # === end popup handling ===

    # 3. Wait for products page
    wait.until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    print("✅ Logged in, on Products page")

    # 4. Click on “Sauce Labs Bolt T-Shirt”
    bolt_tshirt_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sauce Labs Bolt T-Shirt"))
    )
    bolt_tshirt_link.click()
    print("✅ Opened Sauce Labs Bolt T-Shirt detail page")

    # 5. Click "Add to cart"
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
    )
    add_to_cart_button.click()
    print("✅ Added Bolt T-Shirt to cart")

    # 6. Click cart icon
    cart_icon = wait.until(
        EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
    )
    cart_icon.click()
    print("✅ Opened Cart page")

    # 7. Click "Checkout"
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()
    print("✅ Clicked Checkout")

    # 8. Fill First Name, Last Name, Zip
    first_name_box = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name_box = driver.find_element(By.ID, "last-name")
    postal_code_box = driver.find_element(By.ID, "postal-code")

    first_name_box.clear()
    first_name_box.send_keys(FIRST_NAME)

    last_name_box.clear()
    last_name_box.send_keys(LAST_NAME)

    postal_code_box.clear()
    postal_code_box.send_keys(ZIP_CODE)

    # 9. Click "Continue"
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    print("✅ Submitted checkout info (Continue clicked)")

    # 10. Confirm we reached Checkout Overview page
    title_elem = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    print("📦 Now on page:", title_elem.text.strip())  # should be "Checkout: Overview"

    print("\n🎉 End-to-end flow completed successfully.")

finally:
    input("\nPress Enter to close the browser...")
    driver.quit()
