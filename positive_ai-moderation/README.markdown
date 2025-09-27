# Social Media Safe Filter

An open-source **AI Moderation & Positive Content Scoring Engine** built in Python.  
**Social Media Safe Filter** powers content moderation and positivity scoring for the PopBom social media platform, enabling developers to test and filter text content directly from the terminal using the GPT API. This module ensures safe, brand-friendly content while supporting a positive user experience.

---

## ✨ Features

- **AI-Powered Moderation**  
  Classifies text for violence, hate, sexual content, scams, and overall risk.  
  Returns a JSON decision with an action: `allow`, `review`, or `block`.

- **Positive Content Scoring**  
  Assigns a positivity score (0–100) and tags content as uplifting, educational, calm, or neutral.  
  Enables a “Positive-Only” feed mode for curated, brand-safe content.

- **Terminal-Based Testing**  
  Instantly analyze text input in the terminal with moderation and positivity results.

- **Secure Configuration**  
  Store your GPT API key securely using a `.env` file.

---

## 🗂 Project Structure

```
popbom_safefilter/
├── .env                       # Environment variables (e.g., API key)
├── requirements.txt           # Project dependencies
├── main.py                    # Entry point for interactive mode
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
cd popbom-safefilter
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

### 4. Run Interactive Mode

```bash
python main.py
```

The terminal will display:

```
PopBom SafeFilter: AI Moderation & Positive Content Scoring
Type 'quit' to exit.

Enter content to check:
```

Enter any text to receive instant moderation and positivity results.

---

## 📝 Example Output

**Input:**  
`This is a 5-second funny clip about dancing cats.`

**Output:**

```
=== Moderation Result ===
{
  "violence": 0.0,
  "hate": 0.0,
  "sexual": 0.0,
  "scam": 0.0,
  "overallRisk": 0.01,
  "action": "allow",
  "rationale": "Safe and harmless content"
}

=== Positivity Score ===
{
  "positivity": 87,
  "tags": ["uplifting", "funny"],
  "rationale": "Light-hearted and positive content"
}
```

---

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

## 🌟 Why PopBom SafeFilter?

PopBom SafeFilter is a lightweight, developer-friendly Python toolkit designed for social media platforms. It ensures content safety and promotes positive user experiences through AI-powered moderation and positivity scoring. As part of the PopBom ecosystem, it’s ideal for platforms requiring robust, scalable content filtering using GPT models.
