# What's MCP All About?

Model Context Protocol is basically trying to solve the mess of connecting AI apps to different external systems. I like to think of it as the "USB-C for AI" - you know how USB-C just works with everything? That's what MCP is going for. One universal way for LLMs and AI agents to talk to external stuff without all the custom integration headaches.
Here's how it breaks down: you've got MCP Hosts (that's your AI apps needing data) and MCP Servers (the things actually providing that data). The whole point is keeping things clean and modular - you can build these connectors once and reuse them everywhere, plus you get proper security controls baked in.


# How It Actually Works
The architecture is pretty straightforward with three main pieces:
The Server exposes your tools and data through a standard API. The Client is your app talking to that server. And the Adapter - this is where LangChain comes in handy - it handles all the translation between MCP servers and your LLM apps.
The flow goes like this: your LangChain app wants something, the MCP adapter converts that request into MCP format, the server does its thing and sends back results, then the adapter translates everything back so LangChain can actually use it.

# Prerequisites

Before we begin, ensure you have the following:

Python 3.8+ installed
OpenAI API key (for using GPT models with LangChain)
Basic familiarity with LangChain concepts
Terminal access (examples shown on macOS)

# Setting Up the Environment

First, let's create and configure our development environment:

# Reminder to create a virtual environment if you haven't already
python3 -m venv MCP_Demo

# Activate the virtual environment
source MCP_Demo/bin/activate

# Install required packages
pip install langchain-mcp-adapters
pip install langchain-openai
pip install langgraph

# Set your OpenAI API key
export OPENAI_API_KEY=your_api_key

