# 🧠 CoreMind

CoreMind is an autonomous, truth-seeking AI assistant powered by the open-source Mistral language model and live web search via SerpAPI. It’s designed to provide unbiased, human-like summaries of real-time information — free from political filters, commercial agendas, or institutional control.

---

## 🌐 What It Does

- ✅ Pulls live information using [SerpAPI](https://serpapi.com) (Google-powered search)
- ✅ Feeds results into [Mistral](https://mistral.ai)’s LLM (via Ollama) for reasoning
- ✅ Responds conversationally with logic, transparency, and clarity
- ✅ Acknowledges uncertainty and conflicting viewpoints
- ✅ Saves output to local files when needed

---

## ⚙️ Tech Stack

- **Python 3.11**
- [LangChain](https://python.langchain.com/)
- [Mistral LLM](https://ollama.com/library/mistral) (via [Ollama](https://ollama.com))
- [SerpAPI](https://serpapi.com) (search results)
- Pydantic + dotenv

---

## 📦 Setup Instructions

1. **Install dependencies:**

```bash
pip install -r requirements.txt
````

2. **Add your SerpAPI key to `.env`:**

```env
SERPAPI_API_KEY=your_api_key_here
```

3. **Make sure you have Mistral pulled locally:**

```bash
ollama pull mistral
```

4. **Run the app:**

```bash
python main.py
```

---

## 🗣 Example Usage

```txt
You: Who really started COVID-19?

🧠 CoreMind: Based on 5 independent articles, the origins remain debated...
Sources:
1. https://www.dni.gov/...
2. https://www.bbc.com/...
```

---

## 🔐 Project Goals

* 🧠 Rational and independent analysis
* 🔎 Transparent sourcing
* 🚫 No hallucinations
* 🧭 Truth over popularity

---

## 📁 Folder Structure

```
coremind-agent/
│
├── main.py               # Core logic and conversation loop
├── tools.py              # Search, save, and evaluation tools
├── .env                  # (not pushed) SerpAPI key
├── requirements.txt
└── README.md
```

---

## 🔓 License

MIT — use it, modify it, fork it, share it. CoreMind is for everyone who values truth.

---

````

---

✅ Paste this into a new file called `README.md`, then push it with:
git add README.md
git commit -m "Add CoreMind README"
git push
````

Let me know if you’d like a one-line tagline or badge for GitHub display.
