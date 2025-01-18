from phi.playground import Playground, serve_playground_app
from multi_agent import multi_agent

app = Playground(agents=[multi_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)