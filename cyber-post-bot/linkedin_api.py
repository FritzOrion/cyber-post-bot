import requests
import os
from dotenv import load_dotenv

load_dotenv()
ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")

def post_to_linkedin(summary_text, image_path):
    try:
        with open(image_path, "rb") as img_file:
            image_data = img_file.read()

        files = {
            "image": ("cyber_summary.png", image_data, "image/png")
        }
        data = {
            "summary": summary_text
        }

        response = requests.post(ZAPIER_WEBHOOK_URL, data=data, files=files)

        if response.status_code == 200:
            print("✅ Post successfully sent to Zapier.")
            return True
        else:
            print(f"❌ Failed to post. Status code: {response.status_code}")
            print("Response:", response.text)
            return False
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return False
