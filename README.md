# 🎬 DoodStream MP4 Auto Grabber (via Brave + Selenium)

> 🔍 Scraper ini bekerja khusus untuk video DoodStream  
> **yang di-embed di website dengan awalan link: `https://do7go.com/...`**  
> Cocok buat backup video pribadi, arsip kuliah, atau kebutuhan edukasi lainnya.

---

## 🚀 Fitur Utama

```text
✅ Auto ekstrak link video dari halaman do7go.com
✅ Auto buka tiap link dengan Brave Browser
✅ Auto klik tombol play video
✅ Auto grab direct .mp4 link
✅ Hasil disimpan rapi di hasil_mp4_link.txt
```

---

## 📁 Output

```text
📄 hasil.txt
Berisi semua link video do7go.com dari playlist atau halaman

📄 hasil_mp4_link.txt
Berisi direct link .mp4 dari semua video yang berhasil diproses
```

---

## 📦 Instalasi & Requirements

```bash
 ✅ Clone repository dari GitHub
git clone https://github.com/syaibar/DoodStream-MP4-Auto-Grabber-via-Brave-Selenium.git
cd DoodStream-MP4-Auto-Grabber-via-Brave-Selenium

 ✅ Install dependensi Python
pip install requests selenium
```

---

## 🧱 Setup Tambahan

```text
1️⃣ Install Brave Browser
📥 Download dari: https://brave.com

2️⃣ Cari lokasi brave.exe
📂 Biasanya berada di:
C:\Users\NAMA_KAMU\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe

🛠️ Edit di dalam script Python:
BRAVE_PATH = r"C:\Users\NAMA_KAMU\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"

Jika lokasi Brave berbeda, ubah BRAVE_PATH sesuai lokasi file .exe
```

---

## ▶️ Cara Menjalankan

```bash
python "Doodstream Playlist Downloader.py"
```

```text
🔗 Masukkan link playlist / video dari do7go.com:
```

```text
Tool akan otomatis:

📥 Mengambil halaman HTML dari link tersebut
🔗 Mengekstrak semua link video do7go
📄 Menyimpan ke hasil.txt
🧭 Membuka satu per satu link di Brave
▶️ Klik tombol play secara otomatis
🎯 Ambil direct link .mp4
💾 Menyimpan ke hasil_mp4_link.txt
```

---

## ❗ Catatan Penting

```text
🌐 Pastikan koneksi internet kamu stabil saat proses scraping
🔐 Beberapa video mungkin gagal jika dilindungi captcha / login
🖥️ Tool ini dirancang untuk berjalan optimal di Windows
🔕 Semua output error terminal disenyapkan secara otomatis
```

---

## 🛡️ Legalitas & Penggunaan

```text
🚫 Tool ini tidak menyimpan atau mendistribusikan ulang video dari pihak ketiga
🧠 Semua proses dilakukan secara lokal di komputer pribadi kamu
⚠️ Gunakan hanya untuk keperluan pribadi dan edukasi
⚖️ Selalu ikuti hukum dan ketentuan yang berlaku di wilayah kamu
```

---

## 👋 Kontribusi & Lisensi

```text
💡 Proyek ini bersifat open-source
📄 Lisensi: MIT License
🔧 Kamu bebas fork, modifikasi, dan bantu kembangkan lebih lanjut
```

---

## ❤️ Dukung Proyek Ini

```text
🌟 Beri ⭐️ di repo GitHub ini kalau kamu merasa terbantu
☕ Bantu support developer-nya (secangkir kopi 😄)
📩 DM untuk request fitur tambahan
```
