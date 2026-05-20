<<<<<<< HEAD
# agents.py

import os
try:
    import streamlit as st
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
except Exception:
    pass

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

# =========================
# LLM SETUP
# =========================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# =========================
# REACT PROMPT
# =========================

react_prompt = hub.pull("hwchase17/react")

# =========================
# SEARCH AGENT
# =========================

def build_search_agent():

    agent = create_react_agent(
        llm=llm,
        tools=[web_search],
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[web_search],
        verbose=True,
        handle_parsing_errors=True
    )

# =========================
# READER AGENT
# =========================

def build_reader_agent():

    agent = create_react_agent(
        llm=llm,
        tools=[scrape_url],
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[scrape_url],
        verbose=True,
        handle_parsing_errors=True
    )

# =========================
# WRITER CHAIN
# =========================

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert research writer.

Your job is to:
- Write professional reports
- Use structured headings
- Explain concepts clearly
- Summarize research properly
- Keep the writing detailed and factual
"""
    ),
    (
        "human",
        """
Write a detailed research report.

TOPIC:
{topic}

RESEARCH:
{research}
"""
    )
])

writer_chain = writer_prompt | llm | StrOutputParser()

# =========================
# CRITIC CHAIN
# =========================

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a strict research critic.

Your job is to:
- Find weak arguments
- Identify missing information
- Suggest improvements
- Check clarity and structure
"""
    ),
    (
        "human",
        """
Critically review this report.

REPORT:
{report}
"""
    )
])

critic_chain = critic_prompt | llm | StrOutputParser()

=======
# agents.py

import os
try:
    import streamlit as st
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
except Exception:
    pass

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

# =========================
# LLM SETUP
# =========================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# =========================
# REACT PROMPT
# =========================

react_prompt = hub.pull("hwchase17/react")

# =========================
# SEARCH AGENT
# =========================

def build_search_agent():

    agent = create_react_agent(
        llm=llm,
        tools=[web_search],
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[web_search],
        verbose=True,
        handle_parsing_errors=True
    )

# =========================
# READER AGENT
# =========================

def build_reader_agent():

    agent = create_react_agent(
        llm=llm,
        tools=[scrape_url],
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[scrape_url],
        verbose=True,
        handle_parsing_errors=True
    )

# =========================
# WRITER CHAIN
# =========================

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert research writer.

Your job is to:
- Write professional reports
- Use structured headings
- Explain concepts clearly
- Summarize research properly
- Keep the writing detailed and factual
"""
    ),
    (
        "human",
        """
Write a detailed research report.

TOPIC:
{topic}

RESEARCH:
{research}
"""
    )
])

writer_chain = writer_prompt | llm | StrOutputParser()

# =========================
# CRITIC CHAIN
# =========================

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a strict research critic.

Your job is to:
- Find weak arguments
- Identify missing information
- Suggest improvements
- Check clarity and structure
"""
    ),
    (
        "human",
        """
Critically review this report.

REPORT:
{report}
"""
    )
])

critic_chain = critic_prompt | llm | StrOutputParser()

>>>>>>> 2cf9b1cd3b0623547207f82c702b3b0fe41bb59f
