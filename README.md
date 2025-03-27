# Otomoto.pl Scraper

## Description

Otomoto.pl Scraper is a Python script that automatically collects car advertisement data from the Otomoto.pl website. The project allows users to gather information about cars based on a selected make and model, such as price, mileage, year of production, fuel type, gearbox type, and additional details such as engine size and power.

The scraped data is stored in a MySQL database, enabling further analysis, filtering, and automatic updating of records with new offers.

## Features

- **Data Scraping:** Collecting car information based on the selected make and model.
- **Detailed Information Extraction:** Extracting engine size, power, and other details from the listing.
- **MySQL Database:** Storing the scraped data in a MySQL database. A mechanism to ignore duplicates ensures that existing offers are not overwritten.
- **Automation:** The script can be scheduled to run regularly (e.g., daily) to collect and update data in the database.

## Requirements

- Python 3.x
- Python libraries: `selenium`, `mysql-connector`
- ChromeDriver (for browser automation with Selenium)
- MySQL database

## Installation

1. **Install required libraries:**
   
   Use `pip` to install the required dependencies:
   
   ```bash
   pip install selenium mysql-connector
