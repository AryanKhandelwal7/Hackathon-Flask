from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

app = Flask(__name__)
CORS(app)

# Configure ThreadPoolExecutor for async processing
executor = ThreadPoolExecutor(max_workers=10)

# Cache to speed up frequently requested data
@lru_cache(maxsize=128)
def cached_response(url):
    response = requests.get(url)
    return response.content

async def fetch_neRF_image(image_data):
    # Replace with actual NeRF processing endpoint
    neRF_url = "http://your-nerf-server.com/process_image"
    response = await loop.run_in_executor(executor, requests.post, neRF_url, files={'image': image_data})
    return response.content

@app.route('/process_image', methods=['POST'])
async def process_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    # Retrieve image data from request
    image_data = request.files['image'].read()

    # Process image with NeRF
    processed_image = await fetch_neRF_image(image_data)

    # Send the processed image to Unity (or store if needed)
    unity_response = await send_to_unity(processed_image)

    return jsonify({"status": "success", "unity_response": unity_response})

async def send_to_unity(image_data):
    # Replace with your Unity endpoint
    unity_url = "http://your-unity-server.com/upload_image"
    response = await loop.run_in_executor(executor, requests.post, unity_url, files={'image': image_data})
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
