# Gunakan image Selenium dengan Chrome dan ChromeDriver bawaan
FROM selenium/standalone-chrome:latest

# Set user menjadi root agar bisa menjalankan apt-get
USER root

# Atur working directory dalam container
WORKDIR /app

# Update dan install Python serta pip dengan akses root
RUN apt-get update --allow-releaseinfo-change \
    && apt-get install -y python3 python3-pip

# Copy semua file dari proyek ke dalam container
COPY . .

# Install dependencies Python dari requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Perintah untuk menjalankan scraper
CMD ["python3", "scraper.py"]
