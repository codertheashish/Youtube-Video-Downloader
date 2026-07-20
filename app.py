import os
import uuid
import shutil
from flask import Flask, render_template, request, send_file, jsonify, after_this_request
import yt_dlp

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    data = request.get_json(silent=True) or {}
    url = (data.get("url") or "").strip()
    mode = data.get("mode", "video")  # "video" or "audio"

    if not url:
        return jsonify({"error": "Please paste a YouTube link."}), 400

    # Unique subfolder per request so parallel downloads don't clash
    session_id = str(uuid.uuid4())
    session_folder = os.path.join(DOWNLOAD_FOLDER, session_id)
    os.makedirs(session_folder, exist_ok=True)

    outtmpl = os.path.join(session_folder, "%(title)s.%(ext)s")

    if mode == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": outtmpl,
            "noplaylist": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    else:
        ydl_opts = {
            "format": "18/22/best",  # combined audio+video, no ffmpeg needed
            "outtmpl": outtmpl,
            "noplaylist": True,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        shutil.rmtree(session_folder, ignore_errors=True)
        return jsonify({"error": f"Download failed: {str(e)}"}), 500

    files = os.listdir(session_folder)
    if not files:
        shutil.rmtree(session_folder, ignore_errors=True)
        return jsonify({"error": "No file was produced. Try a different link."}), 500

    filepath = os.path.join(session_folder, files[0])

    @after_this_request
    def cleanup(response):
        try:
            shutil.rmtree(session_folder, ignore_errors=True)
        except Exception:
            pass
        return response

    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
