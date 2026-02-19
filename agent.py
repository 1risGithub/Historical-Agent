import os
import logging
import google.cloud.logging

from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.models import Gemini
from google.genai import types
from google.adk.tools import exit_loop

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Logging
google.cloud.logging.Client().setup_logging()
load_dotenv()
model_name = os.getenv("MODEL")
RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, attempts=6)

# ============================================================
# TOOLS
# ============================================================

def append_to_state(tool_context: ToolContext, field: str, content: str):
    existing = tool_context.state.get(field, [])
    tool_context.state[field] = existing + [content]
    logging.info(f"Added to {field}")
    return {"status": "success"}


def write_file(tool_context: ToolContext, filename: str, content: str):
    directory = "historical_output"
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return {"status": "success"}

wiki_tool = LangchainTool(
    tool=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
)

# ============================================================
# AGENTS
# ============================================================

# ============================================================
# Admirer Agent (Positive)
# ============================================================

admirer = Agent(
    name="admirer",
    model=Gemini(model=model_name, retry_options=RETRY_OPTIONS),
    description="Research positive achievements",
    instruction="""
    TOPIC:

    { topic? }

    INSTRUCTIONS:

    Research ONLY positive aspects.

    Use wikipedia tool with keywords like:

    { topic } achievements

    { topic } accomplishments

    { topic } legacy

    Append findings to pos_data
    """,
    tools=[wiki_tool, append_to_state],
)

# ============================================================
# Critic Agent (Negative)
# ============================================================

critic = Agent(
    name="critic",
    model=Gemini(model=model_name, retry_options=RETRY_OPTIONS),
    description="Research negative aspects",
    instruction="""
    TOPIC:

    { topic? }

    INSTRUCTIONS:

    Research ONLY criticisms and controversies

    Use wikipedia tool with:

    { topic } controversy

    { topic } criticism

    { topic } failures

    Append findings to neg_data

    """,
    tools=[wiki_tool, append_to_state],
)

# ============================================================
# Parallel Investigation
# ============================================================

investigation = ParallelAgent(
    name="investigation",
    sub_agents=[
        admirer,
        critic
    ]
)

# ============================================================
# Judge Agent
# ============================================================

judge = Agent(
    name="judge",
    model=Gemini(model=model_name, retry_options=RETRY_OPTIONS),
    description="Ensure balanced research",
    instruction="""
    POSITIVE DATA:

    { pos_data? }

    NEGATIVE DATA:

    { neg_data? }

    INSTRUCTIONS:

    If one side insufficient

    continue research

    If balanced

    use exit_loop

    """,
    tools=[exit_loop],
)

# ============================================================
# Trial Loop
# ============================================================

trial = LoopAgent(
    name="trial",
    sub_agents=[
        investigation,
        judge
    ],
    max_iterations=5,
)

# ============================================================
# Verdict Writer
# ============================================================

verdict_writer = Agent(
    name="verdict_writer",
    model=Gemini(model=model_name, retry_options=RETRY_OPTIONS),
    instruction="""
    Create final balanced report.

    Include:

    TOPIC:

    { topic? }

    POSITIVE:

    { pos_data? }

    NEGATIVE:

    { neg_data? }

    VERDICT:

    Neutral summary

    Use write_file tool

    filename:

    { topic? }.txt

    """,
    tools=[write_file],
)

# ============================================================
# Sequential Court
# ============================================================

court = SequentialAgent(
    name="court",
    sub_agents=[
        trial,
        verdict_writer
    ]
)

# ============================================================
# Root Inquiry Agent
# ============================================================

root_agent = Agent(
    name="inquiry",
    model=Gemini(model=model_name, retry_options=RETRY_OPTIONS),
    instruction="""
    Ask user for historical topic

    Save into topic

    Transfer to court

    """,
    tools=[append_to_state],
    sub_agents=[court]
)
