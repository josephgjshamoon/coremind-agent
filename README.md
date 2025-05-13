# AI Research Agent 🤖📚

An AI-powered research assistant that uses GPT-4o (via LangChain) to answer questions with concise summaries, verified sources, and optional saving to a local text file.

---

### 🔍 What it does
- Uses DuckDuckGo and Wikipedia to gather data  
- Automatically selects tools using LangChain Agents  
- Parses structured output using Pydantic  
- Saves results to `research_output.txt` if needed  

---

### 🚀 How to Use

1. **Clone the repo**

```bash
git clone https://gitlab.com/YOUR_USERNAME/ai-research-agent.git
cd ai-research-agent
```

2. **Create a `.env` file**

```env
OPENAI_API_KEY="your-openai-key-here"
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the script**

```bash
python main.py
```

Enter a research question when prompted:

```
> What is the history of the Eiffel Tower?
```

---

### 🧠 Powered By
- LangChain  
- OpenAI GPT-4o  
- DuckDuckGo Search  
- Wikipedia API  

---

### 📁 Project Structure

| File            | Description                                |
|-----------------|--------------------------------------------|
| `main.py`       | Runs the agent and handles user queries    |
| `tools.py`      | Contains custom tools (search, wiki, save) |
| `.env`          | Stores your OpenAI API key                 |
| `requirements.txt` | Lists required Python packages         |

---

### ✅ Sample Output

```json
{
  "topic": "Eiffel Tower",
  "summary": "The Eiffel Tower is a wrought-iron lattice tower in Paris, constructed in 1889 for the World's Fair.",
  "sources": [
    "https://en.wikipedia.org/wiki/Eiffel_Tower",
    "https://duckduckgo.com/?q=Eiffel+Tower"
  ],
  "tools_used": ["Wikipedia", "DuckDuckGo"]
}
```

---

### 🔐 Note
Do **not** upload your `.env` file or real API key to GitLab.

---


### 🧠 New Features (May 2025 Update)

- ✅ Added **conversation memory** using LangChain’s `ConversationBufferMemory`
- ✅ Agent now supports **multi-turn conversations**, enabling context-aware responses
- ✅ Wrapped in a **chat loop**, allowing continuous dialogue without restarting the script
- ✅ Output is now **structured and readable**, parsed cleanly using JSON