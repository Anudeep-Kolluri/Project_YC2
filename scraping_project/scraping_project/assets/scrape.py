from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
from typing import List

from dagster import asset

@asset
def scrape() -> List:
    """
    Scrape data from internet and return an array after extraction
    Output format -> [["Name", "Description", "Location", "Tags"]]
    """

    SCROLL_COUNT = 3

    URL = "https://www.ycombinator.com/companies"
    SLEEP = 5

    # Set up the options for Firefox
    options = Options()
    options.binary_location = "/usr/bin/firefox"
    options.add_argument("--headless")  # Run in headless mode
    options.log.level = "trace"  # Enable verbose logging

    # Set up the Firefox WebDriver with the Service class
    service = Service(GeckoDriverManager().install())

    print("Starting Firefox...")
    driver = webdriver.Firefox(service=service, options=options)
    print("Firefox started successfully.")

    # Now you can use driver to interact with web pages
    driver.get(URL)

    print("Entered website, loading companies")

    # Initial height of the page
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(SCROLL_COUNT):
        print(f"Loaded page: {i + 1}")
        
        # Scroll to the bottom using JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(SLEEP)

        # Get the new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # Check if scroll height has increased, otherwise break (if no more content is loaded)
        if new_height == last_height:
            print("No more new content to load.")
            break
        last_height = new_height

    print("Scraping Website")
    html = driver.page_source

    # Close the driver
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    company_details = []

    print("Extracting sections")
    for idx, element in enumerate(soup.find_all('a', class_="_company_86jzd_338")):
        title = element.find('span', class_="_coName_86jzd_453").text  # Get company name
        description = element.find('span', class_="_coDescription_86jzd_478").text  # Get company description
        location = element.find('span', class_="_coLocation_86jzd_469").text  # Get company location
        tags = ",".join([tag.text for tag in element.find_all('span', class_="pill _pill_86jzd_33")])  # Get tags
        company_details.append([1000 + idx, title, description, location, tags])

    return company_details

    # print("Loading in pandas DataFrame")
    # df = pd.DataFrame(company_details, columns=["Name", "Description", "Location", "Tags"])

    # df.to_csv("companies.csv", index=False)
    # print("Data saved to companies.csv")



