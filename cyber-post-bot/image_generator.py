from PIL import Image, ImageDraw, ImageFont
import textwrap
from datetime import datetime

def generate_cyber_image(summary_text, output_path="cyber_summary.png"):
    width, height = 1080, 1080
    background_color = "#ffffff"
    text_color = "#111111"
    accent_color = "#0077B5"
    margin = 80

    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 38)

    img = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    title = f"🔐 Weekly Cyber Threats\n📅 {datetime.now().strftime('%A, %B %d, %Y')}"
    draw.multiline_text((margin, margin), title, fill=accent_color, font=title_font, spacing=10)

    formatted = "📌 " + summary_text.replace("\n", "\n📌 ")
    wrapped = textwrap.fill(formatted, width=55)
    draw.multiline_text((margin, margin + 200), wrapped, fill=text_color, font=body_font, spacing=16)

    draw.text((margin, height - 100), "🔗 Stay aware. Stay protected.", fill=accent_color, font=body_font)

    img.save(output_path)
    return output_path
