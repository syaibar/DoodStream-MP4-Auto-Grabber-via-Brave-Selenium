import os
import re
import sys
import time
import logging
import requests
import tempfile
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import LOGGER

# Bungkam log selenium
LOGGER.setLevel(logging.WARNING)

# Jalur Brave
BRAVE_PATH = r"C:\Users\syaibarstudio\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"

# File output
HTML_SOURCE_FILE = "hasil.txt"
OUTPUT_MP4_FILE = "hasil_mp4_link.txt"

# Bungkam error Python
sys.stderr = open(os.devnull, "w")

def extract_video_links(html_text):
    links = re.findall(r'https://do7go\.com/d/[a-zA-Z0-9]+', html_text)
    return list(set(links))

def start_chrome_driver(options):
    tmp_log = open(os.devnull, "w")  # Bungkam output log

    service = Service()
    service.creationflags = subprocess.CREATE_NO_WINDOW
    service.log_output = tmp_log
    service.stdout = tmp_log
    service.stderr = tmp_log

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_video_link(driver):
    try:
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            driver.switch_to.frame(iframes[0])
            print("     🪟 Masuk iframe...")

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "vjs-big-play-button"))
        )
        print("     ✅ Tombol play ditemukan!")

        driver.execute_script("document.querySelector('.vjs-big-play-button').click();")
        print("     ▶️ Play ditekan...")

        time.sleep(10)

        video_src = driver.execute_script("""
            let video = document.querySelector('video');
            if (!video) return "NO_VIDEO";
            let direct = video.getAttribute('src') || video.currentSrc;
            return direct || "NO_SRC";
        """)

        if video_src == "NO_VIDEO":
            print("     ⚠️ <video> tidak ditemukan.")
            return None
        elif video_src == "NO_SRC":
            print("     ⚠️ Video ditemukan tapi src kosong.")
            return None
        else:
            return video_src

    except Exception as e:
        print(f"     ⚠️ Gagal ambil video: {e}")
        return None

def process_page(url):
    options = Options()
    options.binary_location = BRAVE_PATH
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,720")
    options.add_argument("--window-position=9999,9999")
    options.add_argument("--headless=new")
    options.add_argument("--mute-audio")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    try:
        driver = start_chrome_driver(options)
        print(f"     ⏳ Membuka: {url}")
        driver.get(url)
        time.sleep(6)

        try:
            continue_btn = driver.find_element(By.CLASS_NAME, "btn")
            continue_btn.click()
            print("     👉 Klik Continue...")
            time.sleep(6)
        except:
            print("     ℹ️ Tidak ada tombol Continue")

        return get_video_link(driver)

    except Exception as e:
        print(f"     ❌ Gagal proses {url}: {e}")
        return None
    finally:
        try:
            driver.quit()
        except:
            pass

def main():
    print("=== DoodStream Scraper + Grabber MP4 via Brave (Silent & Background Mode) ===\n")

    input_url = input("🔗 Masukkan link playlist / video dari do7go.com: ").strip()

    if not input_url.startswith("https://"):
        print("❌ Link tidak valid.")
        return

    print(f"📥 Mengambil konten dari: {input_url}")

    try:
        response = requests.get(input_url, timeout=15)
        html_content = response.text

        video_links = extract_video_links(html_content)

        if not video_links:
            print("⚠️ Tidak ada link ditemukan.")
            return

        with open(HTML_SOURCE_FILE, "w", encoding='utf-8') as out:
            for link in video_links:
                out.write(link + "\n")

        print(f"\n✅ Ditemukan {len(video_links)} link video. Mulai proses ambil direct MP4...\n")

    except Exception as e:
        print(f"❌ Terjadi error saat ambil HTML: {e}")
        return

    with open(HTML_SOURCE_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip().startswith("https://")]

    with open(OUTPUT_MP4_FILE, "w", encoding="utf-8") as out:
        for idx, url in enumerate(urls, 1):
            print(f"[{idx}] Proses: {url}")
            mp4_link = process_page(url)
            if mp4_link:
                print(f"     ✅ Link ditemukan: {mp4_link}")
                out.write(mp4_link + "\n")
                out.flush()
            else:
                print("     ❌ Gagal menemukan link")

    print(f"\n🎉 Semua link MP4 disimpan di '{OUTPUT_MP4_FILE}'")

if __name__ == "__main__":
    main()
