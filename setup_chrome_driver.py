import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (optional)

    try:
        # Specify the path to your chromedriver.exe
        driver_path = r'chromedriver-win64\chromedriver.exe'  # Use a raw string to avoid escape issues
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error setting up ChromeDriver: {e}")
        sys.exit(1)



# Initialize an empty list to store all the data
all_data = []
headers = []

try:
    driver = setup_driver()

    # Loop through all 51 pages
    for page in range(1, 52):
        url = f"https://mofaga.gov.np/local-contact?page={page}"
        driver.get(url)
        
        # Wait for the table to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "table")))
        
        # Extract table headers (only on the first page)
        if page == 1:
            header_elements = driver.find_elements(By.XPATH, "//table[@class='table']/thead/tr/th")
            headers = [header.text for header in header_elements]
        
        # Find all rows in the table
        rows = driver.find_elements(By.XPATH, "//table[@class='table']/tbody/tr")
        
        # Extract data from each row
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = [column.text for column in columns]
            all_data.append(row_data)
        
        print(f"Processed page {page}")
        time.sleep(1)  # Add a small delay to avoid overwhelming the server

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

finally:
    if 'driver' in locals():
        driver.quit()

# Create a DataFrame using the extracted headers
df = pd.DataFrame(all_data, columns=headers)

# Save to CSV
df.to_csv("local_contact_data.csv", index=False)

print("Data extraction complete. CSV file 'local_contact_data.csv' has been created.")
print(f"Table headers: {headers}")

