# Social Media Safe Filter

A lightweight **AI Moderation & Positive-Only Scoring microservice** built with Python + FastAPI.  
This service powers one part of a larger social media platform by automatically checking **posts** and **comments** for harmful or negative content, and scoring their **positivity** using GPT models.

**Social Media Safe Filter** powers content moderation and positivity scoring for the PopBom social media platform, enabling developers to test and filter text content directly from the terminal using the GPT API. This module ensures safe, brand-friendly content while supporting a positive user experience.

---

## ✨ Features

- **AI Moderation**  
  Checks text content (posts or comments) for violence, hate, sexual content, scams, and overall risk.  
  Returns a structured JSON verdict: `allow`, `review`, or `block`.

- **Positive-Only Scoring**  
  Rates content on positivity (0–100) and tags it as uplifting, educational, calm, or neutral.  
  Enables “Positive-Only” feed mode for safe, brand-friendly content.

- **HTTP API for Easy Integration**  
  A FastAPI microservice that your main backend or frontend can call directly.

- **Secure Key Storage**  
  Uses `.env` to keep your GPT API key safe.

---

## 🗂 Project Structure

```
social_media_safefilter/
├── .env                       # Environment variables (e.g., API key)
├── requirements.txt           # Project dependencies
├── main.py                    # Entry point for interactive mode
├─ server_api.py               # FastAPI microservice
├── moderation.py              # Moderation logic
├── positive_only.py           # Positivity scoring logic
├── prompts/                   # Prompt templates
│   ├── moderation_system.txt  # Moderation classification rules
│   ├── moderation_user.txt    # User input template for moderation
│   ├── positivity_system.txt  # Positivity scoring rubric
│   └── positivity_user.txt    # User input template for positivity
└── utils.py                   # Utility functions
```

---

## 🚀 Getting Started

Follow these steps to set up and run PopBom SafeFilter locally.

### 1. Clone the Repository

```bash
git clone https://github.com/taniajasmin/social-media-safe-filter.git
cd social-media-safe-filter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your API Key

Create a `.env` file in the project root and add your OpenAI API key:

```plaintext
OPENAI_API_KEY=sk-xxxxxx_your_key_here
```

### 4. Run Interactive Mode/ the Server

```bash
uvicorn server_api:app --reload --port 8088
```

#### Visit:
- http://127.0.0.1:8088/ → service info
- http://127.0.0.1:8088/docs → Swagger UI for testing /check endpoint

--- 

## 📝 Example Request

``` Bash
curl -X POST "http://127.0.0.1:8088/check" \
  -H "Content-Type: application/json" \
  -d '{
    "content_id":"post_123",
    "user_id":"u_9",
    "type":"post",
    "text":"Win money fast—click this shady link!",
    "lang":"en",
    "region":"us",
    "audience":"general",
    "positive_only": true
  }'
```

---

## 📝 Example Request

```json
{
  "content_id": "post_123",
  "action": "block",
  "positivity": 12,
  "positive_only_pass": false,
  "safety": {
    "violence": 0,
    "hate": 0,
    "sexual": 0,
    "scam": 0.92,
    "overallRisk": 0.92,
    "action": "block",
    "rationale": "Scam indicators present."
  },
  "rationale": "Scam indicators present."
}
```

---

## 🛠 Integrating Into Your Social Media Backend

- On Post/Comment Create: Call the /check endpoint with the content text and user metadata.
- Store Decision: Save action + positivity in your database.
- Filter Feed: Only show items marked allow or above your positivity threshold for “Positive-Only” mode.
- Review/Block: Route flagged items to moderators or hide automatically.

--- 

## ⚡ Why This Microservice Exists

This is one module of a larger social media project.
It focuses only on content safety and positivity scoring so that the rest of the platform can focus on feed ranking, video hosting, gifting, analytics, etc.

## 🔧 Customizing Prompts

Modify the prompt files in the `prompts/` directory to tailor moderation and positivity criteria:

- `prompts/moderation_system.txt`: Defines rules for content classification.  
- `prompts/positivity_system.txt`: Defines the positivity scoring rubric.

---

## 🛡 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with detailed test cases.

---

## 🌟 Why Social Media Safe Filter?

Social Media Safe Filter is a lightweight, developer-friendly Python toolkit designed for social media platforms. It ensures content safety and promotes positive user experiences through AI-powered moderation and positivity scoring. As part of the PopBom ecosystem, it’s ideal for platforms requiring robust, scalable content filtering using GPT models.
