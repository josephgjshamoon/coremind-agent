from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools import search_tool, wiki_tool, save_tool

import json


load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources:list[str]
    tools_used: list[str]


llm = ChatOpenAI(model="gpt-4o")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an AI-powered research assistant designed to generate concise, well-structured responses.
            Use available tools when helpful. Present your output clearly in the following format:
            \n{format_instructions}
            Respond only with this format and no extra explanation.
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(

    llm=llm,
    prompt=prompt,
    tools=tools
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        break
    raw_response = agent_executor.invoke({"query": query})
    parsed = json.loads(raw_response["output"])
    print("\n🧠 Topic:", parsed["topic"])
    print("📝 Summary:", parsed["summary"])
    print("🔗 Sources:", ", ".join(parsed["sources"]))
    print("🛠 Tools Used:", ", ".join(parsed["tools_used"]))