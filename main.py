import json
from time import time, sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

def parse():
    driver = webdriver.Chrome()
    max_page = 3

    wait = WebDriverWait(driver, 5)

    result = []

    for page in range(1, max_page):
        driver.get(f'https://jobs.marksandspencer.com/job-search?page={page}')

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-Hits')))

        jobs = driver.find_elements(By.CLASS_NAME, 'ais-Hits-item')
        for job in jobs:
            title = job.find_element(By.CSS_SELECTOR, "div > div > h3.text-2xl").text
            url = job.find_element(By.CSS_SELECTOR, "div > div > div > a.c-btn").get_attribute('href')

            result.append({
                'url': url,
                'title': title
            })

    driver.quit()

    with open('result.json', 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    parse()