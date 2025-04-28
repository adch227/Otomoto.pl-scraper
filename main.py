from crawler import OtomotoScraper
from database import MySQLHandler
from config import db_config

#Konfiguracja scrapera - wybranie marki/modelu
scraper = OtomotoScraper(marka='mazda', model='cx-3', chromedriver_path="E:/Quant 2025/Selenium/chromedriver.exe")

#Pobranie danych
scraped_data = scraper.run()

#Konfiguracja bazy danych w pliku config
mysql_handler = MySQLHandler(db_config)

#Zapis do MySQL
mysql_handler.insert_data(scraped_data)

#Zamknięcie połączenia
mysql_handler.close_connection()
