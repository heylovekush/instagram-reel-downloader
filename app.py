from flask import Flask, request, jsonify, render_template
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.json["url"]
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        return jsonify({"video": info["url"]})

app.run(host="0.0.0.0", port=10000)
