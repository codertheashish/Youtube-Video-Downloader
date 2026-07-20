# 🎬 YouTube Downloader (Web App)

A simple, clean web app to download YouTube videos as **MP4** or extract audio as **MP3** — just paste a link and hit Download.

Built with **Flask** + **yt-dlp**, single-page frontend, no clutter.

## ✨ Features
- Paste any YouTube video URL
- Choose **Video (MP4)** or **Audio (MP3)**
- One-click download — browser saves the file directly
- Clean, responsive single-page UI
- No accounts, no ads, no extra steps

## 🛠️ Tech Stack
- Python, Flask (backend + API)
- yt-dlp (download engine)
- HTML, CSS, vanilla JS (frontend)

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/codertheashish/Youtube-Video-Downloader.git
cd youtube-downloader
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg (required for MP3 audio extraction)
- **Windows:** download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
- **Mac:** `brew install ffmpeg`
- **Linux:** `sudo apt install ffmpeg`

### 4. Run the app
```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

## 📂 Project Structure
```
youtube-downloader/
├── app.py                # Flask backend
├── requirements.txt
├── templates/
│   └── index.html        # Main page
└── static/
    ├── style.css
    └── script.js
```

## ⚠️ Disclaimer
This project is for **personal and educational use only**. Please respect YouTube's Terms of Service and only download content you have the right to download.

## 👤 Author
**Ashish Kumar Prajapati**
- GitHub: [@codertheashish](https://github.com/codertheashish)
- Portfolio: [codertheashish.vercel.app](https://codertheashish.vercel.app)
