#Search for a product and print first 5 result titles


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    wait = WebDriverWait(driver, 20)

    # 1. Wait for search box and search for "laptop"
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("laptop")
    search_box.submit()

    # 2. Wait until at least one search result card is present
    result_cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
        )
    )

    print(f"Total result cards found: {len(result_cards)}")

    titles = []

    # 3. From each card, try to get the title using different methods
    for card in result_cards:
        title_text = ""

        # Method 1: h2 element text
        try:
            h2 = card.find_element(By.TAG_NAME, "h2")
            title_text = h2.text.strip()
        except Exception:
            pass

        # Method 2: anchor under h2
        if not title_text:
            try:
                a_tag = card.find_element(By.CSS_SELECTOR, "h2 a")
                title_text = a_tag.text.strip()
            except Exception:
                pass

        # Method 3: any span inside h2
        if not title_text:
            try:

                span = card.find_element(By.CSS_SELECTOR, "h2 a span")
                title_text = span.text.strip()
            except Exception:
                pass

        if title_text:
            titles.append(title_text)

        if len(titles) >= 5:
            break  # we only need top 5

    print("Top 5 product titles:")
    if not titles:
        print("No titles were extracted. Page layout or CAPTCHA may be blocking results.")
    else:
        for i, title in enumerate(titles, start=1):
            print(f"{i}. {title}")

finally:
    driver.quit()
