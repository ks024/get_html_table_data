# HTML Table Data Scraper

This project is a web scraper that extracts local contact information from the [Mofaga Government website](https://mofaga.gov.np/local-contact) using Selenium. The scraped data is saved as a CSV file for further analysis.

## Features

- Scrapes data from multiple pages.
- Extracts specific contact details and links.
- Saves the collected data in a structured CSV format.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads) (Ensure it matches your Chrome version)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ks024/get_html_table_data.git
   cd get_html_table_data
   ```

2. Install the required Python packages:

   ```bash
   pip install selenium pandas
   ```

3. Ensure that you have the ChromeDriver executable in the specified path:

   ```bash
   chromedriver-win64/chromedriver.exe
   ```

## Usage

Run the script using the following command:

```bash
python main.py
```

This will start the scraping process. The output will be saved in a file named `local_contact_data.csv` in the same directory.

## Code Overview

The main components of the script include:

- **Setup Driver**: Initializes the Chrome WebDriver with appropriate options.
- **Data Extraction**: Loops through the specified pages, retrieves table headers and rows, and collects data.
- **CSV Output**: Saves the extracted data into a CSV file.

## Error Handling

The script includes basic error handling for:

- Driver setup failures
- Timeouts while waiting for elements
- Mismatches in expected row data

## Acknowledgements

- [Selenium](https://www.selenium.dev/) for browser automation
- [Pandas](https://pandas.pydata.org/) for data manipulation and CSV output
