from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Konfigurasi ChromeDriver untuk Railway
chrome_options = Options()
chrome_options.add_argument("--headless")  # Mode tanpa UI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Lokasi ChromeDriver (Railway sudah menyediakannya)
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

def download_idx_data(tanggal):
    url = "https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/"
    driver.get(url)
    
    time.sleep(5)  # Tunggu halaman load
    
    # Pilih tanggal (pastikan ID sesuai dengan HTML terbaru)
    date_input = driver.find_element(By.ID, "datePickerId")
    date_input.clear()
    date_input.send_keys(tanggal)
    
    # Klik tombol unduh
    download_button = driver.find_element(By.CLASS_NAME, "download-button-class")
    download_button.click()
    
    time.sleep(5)  # Tunggu file terunduh
    print(f"Data {tanggal} berhasil diunduh.")

# Contoh scraping beberapa tanggal
tanggal_list = ["01-03-2024", "02-03-2024"]
for tanggal in tanggal_list:
    download_idx_data(tanggal)

# Tutup browser
driver.quit()
