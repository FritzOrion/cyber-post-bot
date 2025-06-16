# 🛡️ Cybersecurity Threat Summary Bot

This bot generates a weekly cybersecurity threat summary using GPT-4 and auto-posts it to LinkedIn via Zapier — with a custom image for professional flair.

## 🔧 Setup

1. `pip install -r requirements.txt`
2. Create `.env` from `.env.example`
3. Add your OpenAI key + Zapier Webhook
4. Run: `python main.py`

## 🖼️ Example Post

- GPT-written summary
- Image: 1080x1080 with title + bullets
- Zapier uploads it to LinkedIn

## 🗓️ Schedule (Optional)

Use `cron`, `APScheduler`, or Task Scheduler to run `main.py` every Tuesday and Thursday.
