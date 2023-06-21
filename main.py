import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv(".env")
os.environ["OPENAI_API_KEY"]  = os.getenv("OPENAI_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

# pip install google-search-results
llm = OpenAI(model_name="text-davinci-003",
             max_tokens=200,
             temperature=0)

tool_names = ["serpapi"]
tools = load_tools(tool_names)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("What is Air Pods Pro 2?")
agent.run("who is the domestic ranking of USC in 2023")