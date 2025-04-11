# 🎬 DoodStream MP4 Auto Grabber (via Brave + Selenium)

Tool ini dibuat untuk membantu kamu mengambil direct link `.mp4` dari website **do7go.com** secara otomatis.  
Cocok digunakan untuk backup video pribadi, arsip kuliah, atau kebutuhan edukasi lainnya.

---

## 🚀 Fitur Utama

- ✅ Auto ekstrak link video dari halaman do7go.com
- ✅ Auto buka tiap link dengan **Brave Browser**
- ✅ Auto klik tombol play video
- ✅ Auto grab direct `.mp4` link
- ✅ Hasil disimpan rapi di `hasil_mp4_link.txt`

---

## 📁 Output

| File                  | Isi                                                |
|-----------------------|----------------------------------------------------|
| `hasil.txt`           | Semua link video do7go.com dari playlist / halaman |
| `hasil_mp4_link.txt`  | Direct `.mp4` links setelah diproses di browser    |

---

## 📦 Instalasi & Requirements

### ✅ Python 3.7 atau lebih baru

### ✅ Install Dependensi

```bash
pip install -r requirements.txt
```

---

## 🧱 Setup Tambahan

```plaintext
1️⃣ Install Brave Browser
🔗 Download dari:
https://brave.com

2️⃣ Cari Lokasi brave.exe
📁 Biasanya terletak di:
C:\Users\NAMA_KAMU\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe

🛠️ Contoh setting di script Python:
BRAVE_PATH = r"C:\Users\NAMA_KAMU\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"

💡 Jika lokasi Brave kamu berbeda, ganti BRAVE_PATH sesuai letak brave.exe di PC kamu.
```

---

## ▶️ Cara Menjalankan

```bash
python script.py
```

Saat diminta, masukkan link playlist / video dari do7go.com:

```text
🔗 Masukkan link playlist / video dari do7go.com:
```

Tool akan otomatis:

```text
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
Tool ini tidak menyimpan atau mendistribusikan ulang video dari pihak ketiga.
Semua proses dilakukan lokal di komputer pribadi kamu.

⚠️ Gunakan hanya untuk keperluan pribadi dan edukasi.
⚖️ Selalu ikuti hukum dan ketentuan yang berlaku di wilayah kamu.
```

---

## 👋 Kontribusi & Lisensi

```text
💡 Proyek ini bersifat open-source
📄 Lisensi: MIT License
🧠 Kamu bebas fork, modifikasi, dan bantu kembangkan lebih lanjut
```

---

## ❤️ Dukung Proyek Ini

```text
⭐ Beri bintang di repo GitHub ini kalau kamu merasa terbantu
☕ Bantu support developer-nya
📨 DM untuk request fitur tambahan
```
