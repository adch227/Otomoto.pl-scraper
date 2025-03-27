from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class OtomotoScraper:
    def __init__(self, marka, model, chromedriver_path):
        self.marka = marka
        self.model = model
        self.url = f"https://www.otomoto.pl/osobowe/{marka}/{model}"
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.data = []
        self.max_pages = 1

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.send_keys(Keys.ENTER)
        except:
            pass 

    def get_max_pages(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ooa-6ysn8b"))
            )
            pages = self.driver.find_elements(By.CLASS_NAME, "ooa-6ysn8b")
            self.max_pages = int(pages[-1].text) if pages else 1
        except:
            self.max_pages = 1

    def extract_data(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "ooa-vtik1a"))
        )

        name_elements = self.driver.find_elements(By.CLASS_NAME, "ei3upbu0")
        details_elements = self.driver.find_elements(By.CLASS_NAME, "eztwrb60")
        price_elements = self.driver.find_elements(By.CLASS_NAME, "e149hmnd1")
        mileage_elements = self.driver.find_elements(By.XPATH, "//dd[@data-parameter='mileage']")
        fuel_elements = self.driver.find_elements(By.XPATH, "//dd[@data-parameter='fuel_type']")
        gearbox_elements = self.driver.find_elements(By.XPATH, "//dd[@data-parameter='gearbox']")
        year_elements = self.driver.find_elements(By.XPATH, "//dd[@data-parameter='year']")

        names = [e.text for e in name_elements]
        details = [e.text for e in details_elements]
        prices = [e.text for e in price_elements]
        mileages = [e.text for e in mileage_elements]
        fuels = [e.text for e in fuel_elements]
        gearboxes = [e.text for e in gearbox_elements]
        years = [e.text for e in year_elements]

        def extract_engine_power_from_details(details_text):
            parts = [p.strip() for p in details_text.split("•")]
            engine = parts[0] if len(parts) > 0 else "Brak danych"
            power = parts[1] if len(parts) > 1 else "Brak danych"
            rest_details = " • ".join(parts[2:]) if len(parts) > 2 else "Brak danych"
            return engine, power, rest_details

        for i in range(len(names)):
            engine, power, rest_details = extract_engine_power_from_details(details[i] if i < len(details) else "")

            self.data.append({
                "Name": names[i] if i < len(names) else "Brak danych",
                "Engine": engine,
                "Power": power,
                "Price": prices[i] if i < len(prices) else "Brak danych",
                "Mileage": mileages[i] if i < len(mileages) else "Brak danych",
                "Fuel": fuels[i] if i < len(fuels) else "Brak danych",
                "Gearbox": gearboxes[i] if i < len(gearboxes) else "Brak danych",
                "Year": years[i] if i < len(years) else "Brak danych",
                "Details": rest_details,
            })

    def run(self):
        self.driver.get(self.url)
        self.accept_cookies()
        time.sleep(2)
        self.get_max_pages()
        
        for page in range(1, self.max_pages + 1):
            print(f"Scraping page {page}/{self.max_pages}")
            self.driver.get(f"{self.url}?page={page}")
            time.sleep(2)
            self.extract_data()

        self.driver.quit()
        return self.data
