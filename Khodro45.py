from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import arabic_reshaper
from bidi.algorithm import get_display
import time

all_arr = []

url = "https://khodro45.com/used-car/"

chrome_options = Options()
service = Service(executable_path=r"C:/Program Files/Google/Chrome/Application/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


try:
    driver.get(url)

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".col-12.mb-4.position-relative.col-md-4"))
    )

    news_list = driver.find_elements(By.CSS_SELECTOR, ".col-12.mb-4.position-relative.col-md-4")

    for news in news_list:
        news_text = news.text.split('\n')
        reshaped_text = [line for line in news_text]
        bidi_text = [line for line in reshaped_text]
        print(bidi_text)
        arr = {
            "PostDate": bidi_text[7],
            "Feature": bidi_text[0],
            "Car": bidi_text[1],
            "Model": bidi_text[2],
            "Year": bidi_text[3],
            "Price": bidi_text[5],
            "Kilometer": bidi_text[8],
            "Options": bidi_text[9],
            "Document": bidi_text[10],
            "Location" : bidi_text[11]
        }
        all_arr.append(arr)

finally:
    driver.quit() 

import pandas as pd

df = pd.DataFrame(all_arr)

file_path = "F:\\DA\\Projects\\Khodro45.xlsx"

try:
    existing_df = pd.read_excel(file_path)
    updated_df = pd.concat([existing_df, df], ignore_index=True)
except FileNotFoundError:
    updated_df = df

updated_df.to_excel(file_path, index=False)

# df.to_excel("F:\\DA\\DA 07\\DA 07\\khodro45.xlsx", index=False)
