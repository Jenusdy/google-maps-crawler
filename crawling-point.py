from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
from bs4 import BeautifulSoup

pd.options.display.max_columns = None

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 5)

driver.get('https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/utils/geocoder')
input_field = wait.until(EC.presence_of_element_located((By.ID, "query-input")))


def getAlamat(html):
    # Ekstrak Alamat dari Result
    alamat_point = html.find(class_="result-formatted-address").get_text()
    alamat_point = re.sub(' +', ' ', alamat_point)
    alamat_point = alamat_point.replace('\n', '')
    return alamat_point.replace('Address: ', '')


def getGeolokasi(html):
    # Geolocation
    geolocation = html.find(class_="result-location").get_text()
    geolocation = re.sub(' +', ' ', geolocation)
    geolocation = geolocation.replace('\n', '')
    geolocation = geolocation.replace('Location: ', '')
    geolocation = geolocation.split(' ')[0]
    geolocation = geolocation.split(',')
    latitude_point = geolocation[0]
    longitude_point = geolocation[1]
    return latitude_point, longitude_point


def getTipe(html):
    # Result Types
    tipe_point = html.find(class_="result-types").get_text()
    tipe_point = re.sub(' +', ' ', tipe_point)
    tipe_point = tipe_point.replace('\n', '')
    tipe_point = tipe_point.replace('Types: ', '')
    return tipe_point


df = pd.read_csv('input.csv', sep=',', dtype=object)

for i, r in df.iterrows():
    # Melakukan Clear Input
    input_field.clear()

    # Mengambil Nama Lokasi lalu mengisikan ke dalam Input Field Lokasi
    text_to_insert = r['Nama Lokasi']
    input_field.send_keys(text_to_insert)

    # Melakukan referensi terhadap tombol geocode lalu menekan tombol cari lokasi
    button = wait.until(EC.presence_of_element_located((By.ID, "geocode-button")))
    button.click()
    time.sleep(5)

    try:
        element_xpath_ok = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[12]/div/div/div[1]/p[1]/span')))

        result_address = wait.until(EC.presence_of_element_located((By.ID, "result-0")))
        html_content = result_address.get_attribute("innerHTML")

        # Print the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        alamat = getAlamat(soup)
        latitude, longitude = getGeolokasi(soup)
        tipe = getTipe(soup)

        df.loc[df.index == i, 'latitude'] = latitude
        df.loc[df.index == i, 'longitude'] = longitude
        df.loc[df.index == i, 'alamat'] = alamat
        df.loc[df.index == i, 'tipe'] = tipe

    except AttributeError:
        print(i, "Tidak ada ditemukan")
    except TimeoutException:
        print(i, "Tidak ada ditemukan")

df.to_csv('result.csv', sep=',', escapechar=',', index=False)
