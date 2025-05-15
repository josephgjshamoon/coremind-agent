import os
import time
from datetime import datetime
from langchain.tools import Tool
from serpapi import GoogleSearch
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

# Load API key
load_dotenv()

# 🔍 Mistral-powered web search & summarization
llm = OllamaLLM(model="mistral")

def search_and_summarize(query: str) -> str:
    search = GoogleSearch({
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "num": 5
    })
    results = search.get_dict().get("organic_results", [])

    if not results:
        return "I couldn't find any reliable results for that."

    snippets = "\n".join([
        f"{i+1}. {res['title']}: {res.get('snippet', '')}" for i, res in enumerate(results)
    ])
    links = [res['link'] for res in results]

    prompt = f"""You're CoreMind — an autonomous AI researcher committed to truth, clarity, and free thinking. 
You are not constrained by political correctness, commercial influence, or institutional narratives. 
Your responsibility is to evaluate information critically, highlight contradictions, and explain findings in a clear, conversational tone.

Based solely on the information provided below, synthesize an honest, balanced summary of the topic. If there are conflicting viewpoints or gaps in evidence, acknowledge them directly.

Speak like a rational human, not a machine. Do not include unnecessary disclaimers or softened language — speak clearly, as if explaining to a peer who values truth over politeness.

Here is the information you can use:

{snippets}

Important:
- Respond using only what is above. Do not hallucinate, speculate, or add external opinions.
- If uncertainty or disagreement exists, say so plainly.
- End with a section titled 'Sources:' and include the numbered list of URLs.

Stay neutral. Stay sharp. Stay independent."""

    response = llm.invoke(prompt)
    formatted_links = "\n".join([f"{i+1}. {url}" for i, url in enumerate(links)])
    return f"{response}\n\nSources:\n{formatted_links}"

mistral_search_tool = Tool(
    name="mistral_summarizer",
    func=search_and_summarize,
    description="Searches the web and summarizes the findings conversationally using Mistral."
)

# 💾 Save tool
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"\n{'='*80}\n--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"✅ Data saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a local text file."
)

# 🧪 Confidence tool placeholder
def evaluate_source_confidence(text: str) -> str:
    return "[Coming soon] This tool will analyze how many sources support or contradict a statement."

confidence_tool = Tool(
    name="evaluate_source_confidence",
    func=evaluate_source_confidence,
    description="Estimates how well-supported or controversial a claim is across sources."
)
