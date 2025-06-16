from threat_summary import get_cyber_threat_summary
from image_generator import generate_cyber_image
from linkedin_api import post_to_linkedin

def job():
    summary = get_cyber_threat_summary()

    # Emojify the post text
    header = "🚨 Weekly Cybersecurity Threat Brief\n\n"
    footer = "\n🧠 Stay informed. 🔒 Stay secure."
    full_summary = f"{header}{summary}{footer}"

    image_path = generate_cyber_image(full_summary)
    success = post_to_linkedin(full_summary, image_path)

    if success:
        print("🎉 Post completed.")
    else:
        print("⚠️ Post failed.")

if __name__ == "__main__":
    job()
