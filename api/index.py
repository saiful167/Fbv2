from flask import Flask, request, jsonify, render_template_string
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Facebook API Endpoint
FB_API_URL = "https://fbdownloaderhd.com/wp-json/aio-dl/video-data/"

@app.route('/')
def home():
    return render_template_string(open('index.html').read())

@app.route('/api/facebook', methods=['GET'])
def fetch_facebook_video():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "Facebook URL is required", "developer": "Saiful Islam"}), 400

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://fbdownloaderhd.com/facebook-video-downloader/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # ফেসবুকের ওই এপিআইতে রিকোয়েস্ট পাঠানো
        response = requests.post(FB_API_URL, json={"url": video_url}, headers=headers)
        data = response.json()
        
        # আপনার ব্র্যান্ডিং ডাটা
        data["developer"] = "Saiful Islam"
        data["contact"] = "saifulsajedul@gmail.com"
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e), "developer": "Saiful Islam"}), 500

app = app
