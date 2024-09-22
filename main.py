from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import sys

def setup_driver():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--window-size=1920,1080")

    try:
        driver_path = r'chromedriver-win64\chromedriver.exe'
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error setting up ChromeDriver: {e}")
        sys.exit(1)

all_data = []
headers = []

try:
    driver = setup_driver()

    for page in range(1, 52):  # Scrape all 51 pages
        url = f"https://mofaga.gov.np/local-contact?page={page}"
        driver.get(url)
        
        table_xpath = "//table[@class='table table-striped table-hover table-bordered']"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, table_xpath)))
        
        if page == 1:
            header_elements = driver.find_elements(By.XPATH, f"{table_xpath}/thead/tr/th")
            headers = [header.text for header in header_elements]
        
        rows = driver.find_elements(By.XPATH, f"{table_xpath}/tbody/tr")
        
        rows_processed = 0
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = []
            for i, column in enumerate(columns):
                if i == 4:  # Fifth column (index 4)
                    try:
                        link = column.find_element(By.TAG_NAME, "a")
                        row_data.append(link.get_attribute("href"))
                    except NoSuchElementException:
                        row_data.append("")  # Add empty string if no link found
                else:
                    row_data.append(column.text)
            
            if len(row_data) == len(headers):  # Basic validation
                all_data.append(row_data)
                rows_processed += 1
            else:
                print(f"Skipped a row on page {page} due to column mismatch")
        
        print(f"Processed page {page} of 51 ({rows_processed} rows)")
        time.sleep(1)  # Add a small delay to avoid overwhelming the server

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

finally:
    if 'driver' in locals():
        driver.quit()


# Output CSV
try:
    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv("local_contact_data.csv", index=False, encoding='utf-8')
    print("Data extraction complete. CSV file 'local_contact_data.csv' has been created.")
    print(f"Total rows extracted: {len(df)}")
except Exception as e:
    print(f"Failed to write CSV: {e}")