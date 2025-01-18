from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search web for any latest information you need",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    markdown=True,
    show_tool_calls=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent = Agent(
    name="Multi Agent",
    team=[web_search_agent, finance_agent],
    instructions=["Always include the steps you are taking and your reasoning process"],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app(app)

# st.title("Multi Agent")

# st.text("This is a multi-agent system that can help you with web search and finance information")
# st.text("You can ask any question related to finance or search for any information on the web")

# question = st.text_input("Ask any question", key="question")

# response = multi_agent.run(question)

# if question:
#     st.write(response.content)
