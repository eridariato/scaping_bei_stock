# Gunakan image Python yang sudah memiliki Chrome dan ChromeDriver
FROM selenium/standalone-chrome:latest

# Set working directory di dalam container
WORKDIR /app

# Install Python dan pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy semua file ke dalam container
COPY . .

# Install dependencies dari requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Jalankan script saat container dimulai
CMD ["python3", "scraper.py"]
