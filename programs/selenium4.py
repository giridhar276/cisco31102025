
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    wait = WebDriverWait(driver, 20)

    # 1. Search for "smartphone"
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("smartphone")
    search_box.submit()

    # 2. Wait for search result cards
    result_cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
        )
    )

    print("Total result cards found:", len(result_cards))

    product_link_element = None
    chosen_card_index = None

    # 3. Find first card that has a product link with href containing "/dp/"
    for idx, card in enumerate(result_cards, start=1):
        try:
            # any anchor that goes to a product details page
            link = card.find_element(By.CSS_SELECTOR, "a[href*='/dp/']")
            link_text = link.text.strip()
            #
            # sometimes .text might be empty; still we can use this as a valid product link
            product_link_element = link
            chosen_card_index = idx
            print(f"Using card #{idx}. Link text (may be short/empty): {link_text}")
            break
        except Exception:
            continue

    if product_link_element is None:
        print("Could not find a /dp/ product link in any card.")
    else:
        # 4. Click the product link
        product_link_element.click()

        # Switch to new tab if opened there
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])

        # 5. Wait for product title
        title_elem = wait.until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )
        product_title = title_elem.text.strip()
        print("Product title (product page):", product_title)

        # 6. Get product price
        price_text = "Price not found"

        try:
            # Most common pattern for visible price
            price_elem = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "span.a-price span.a-offscreen")
                )
            )
            price_text = price_elem.text.strip()
        except Exception:
            # Older fallback IDs
            for pid in ["priceblock_ourprice", "priceblock_dealprice"]:
                try:
                    elem = driver.find_element(By.ID, pid)
                    if elem.text.strip():
                        price_text = elem.text.strip()
                        break
                except Exception:
                    continue

        print("Price:", price_text)

finally:
    driver.quit()
