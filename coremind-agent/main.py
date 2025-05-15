from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import OllamaLLM
from langchain.memory import ConversationSummaryBufferMemory
from tools import mistral_search_tool, save_tool, confidence_tool

import json

AGENT_NAME = "CoreMind"

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

tools = [mistral_search_tool, save_tool, confidence_tool]

memory = ConversationSummaryBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    llm = OllamaLLM(model="mistral"),
    max_token_limit=1000
)

# Tool router
def route_query_to_tool(query: str) -> str:
    lowered = query.lower()

    if "search" in lowered or "find" in lowered or "tell me" in lowered or "what is" in lowered:
        return mistral_search_tool.run(query)
    elif "save" in lowered or "write" in lowered:
        return save_tool.run(query)
    elif "evaluate" in lowered or "trust" in lowered or "conflict" in lowered:
        return confidence_tool.run(query)
    else:
        return mistral_search_tool.run(query)

print(f"\n🤖 {AGENT_NAME} activated. Type your question below, or type 'exit' to quit.\n")

while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        break

    tool_result = route_query_to_tool(query)

    parsed = ResearchResponse(
        topic="User Query",
        summary=tool_result,
        sources=["Search + Mistral"],
        tools_used=["Mistral summarizer"]
    )

    print("\n🧠 Topic:", parsed.topic)
    print(f"\033[93m📝 Summary: {parsed.summary}\033[0m")
    print("🔗 Sources:", ", ".join(parsed.sources))
