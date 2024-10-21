import requests
import time
import logging
from datetime import datetime

# Configureer logging


# Basisconfiguratie voor de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("website_monitoring.log"),
                        logging.StreamHandler()
                    ])

websites = ["https://eventalixaccept.org/faq", "https://eventalix.org/faq"]

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Website {url} is up. Status code: {response.status_code}.")            
        else:
            logging.warning(f"Website {url} is down. Status code: {response.status_code}.")            
    except requests.RequestException as e:
        logging.error(f"Error accessing {url}: {e}")

def monitor_websites(interval):
    while True:
        for website in websites:
            check_website(website)
        time.sleep(interval)

# Start monitoring met een interval van 300 seconden (5 minuten)
monitor_websites(10)


