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
