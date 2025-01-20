# Finance agent - phidata

This project is a **Streamlit** application that leverages **OpenAI models** and the `phi` framework to create a multi-agent system. The application provides users with the ability to ask questions and retrieve relevant responses from two specialized agents:

1. **Web Search Agent:** Fetches the latest information from the web using DuckDuckGo.
2. **Finance Agent:** Provides financial data such as stock prices, analyst recommendations, company information, and news using YFinanceTools.

---

## Features

### Web Search Agent
- Uses DuckDuckGo to fetch the latest information.
- Responds to general queries with accurate, real-time information.
- Displays detailed steps and reasoning for each query.

### Finance Agent
- Provides detailed financial data:
  - Stock prices
  - Analyst recommendations
  - Company information
  - Recent company news
- Presents data in table format for clarity and better visualization.

### Multi-Agent System
- Combines both agents into a cohesive system:
  - Routes questions to the appropriate agent based on the context.
  - Includes reasoning steps in responses for better transparency.

---

## Prerequisites

1. Python 3.8 or later
2. Required libraries:
   - `phidata`
   - `streamlit`
   - `python-dotenv`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Environment Setup
Environment Variables: `.env`

OPENAI_API_KEY=your_openai_api_key
PHI_API_KEY=your_phi_api_key


## How to Run
```bash
git clone https://github.com/yourusername/multi-agent-system.git
cd multi-agent-system
```

2. ```bash
   streamlit run app.py
   ```
