from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (tanpa UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path ke ChromeDriver (Pastikan sesuai dengan server/host)
chrome_driver_path = "/usr/bin/chromedriver"  # Ganti sesuai lokasi ChromeDriver di server

# Inisialisasi driver Selenium
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def download_idx_data(tanggal):
    base_url = "https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/"
    driver.get(base_url)
    
    time.sleep(5)  # Tunggu beberapa detik untuk loading
    
    # Pilih tanggal (sesuaikan dengan HTML website terbaru)
    date_input = driver.find_element(By.ID, "datePickerId")  # Sesuaikan dengan ID/Selector tanggal
    date_input.clear()
    date_input.send_keys(tanggal)
    
    # Klik tombol download
    download_button = driver.find_element(By.CLASS_NAME, "download-button-class")  # Sesuaikan dengan class
    download_button.click()
    
    time.sleep(5)  # Tunggu proses download
    
    print(f"Data untuk {tanggal} berhasil diunduh.")

# Contoh download beberapa tanggal
tanggal_list = ["01-03-2024", "02-03-2024"]  # Format bisa disesuaikan
for tanggal in tanggal_list:
    download_idx_data(tanggal)

# Tutup driver
driver.quit()
