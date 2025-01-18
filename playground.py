from phi.playground import Playground, serve_playground_app
from multi_agent import finance_agent, web_search_agent, multi_agent

app = Playground(agents=[finance_agent, web_search_agent, multi_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app(app)