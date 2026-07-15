from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv
from pathlib import Path
import re
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
env_path = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=env_path)

print("Looking for:", env_path)
print("Exists:", env_path.exists())

print("GROQ:", bool(os.getenv("GROQ_API_KEY")))
print("TAVILY:", bool(os.getenv("TAVILY_API_KEY")))

# -----------------------------
# LLM
# -----------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ===================================================
# SEARCH AGENT
# ===================================================

class SearchAgent:

    def invoke(self, topic: str):

        print("Searching the web...\n")

        return web_search.invoke(
            {
                "query": topic
            }
        )


def build_search_agent():

    return SearchAgent()


# ===================================================
# READER AGENT
# ===================================================

class ReaderAgent:

    def invoke(self, search_results: str):

        urls = re.findall(r"URL:\s*(https?://\S+)", search_results)

        if not urls:

            return "No URL found."

        best_url = urls[0]

        print(f"\nReading:\n{best_url}\n")

        return scrape_url.invoke(
            {
                "url": best_url
            }
        )


def build_reader_agent():

    return ReaderAgent()


# ===================================================
# WRITER
# ===================================================

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert research writer."
        ),
        (
            "human",
            """
Topic:
{topic}

Research:

{research}

Write a professional report.

Include

1. Introduction

2. Key Findings

3. Conclusion

4. Sources
"""
        ),
    ]
)

writer_chain = writer_prompt | llm | StrOutputParser()

# ===================================================
# CRITIC
# ===================================================

critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert reviewer."
        ),
        (
            "human",
            """
Review this report.

{report}

Give

Score: X/10

Strengths

Weaknesses

Suggestions
"""
        ),
    ]
)

critic_chain = critic_prompt | llm | StrOutputParser()