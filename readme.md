# AI Competitive Intelligence Agent

This project is an AI-powered competitive analysis agent built using LangChain, Groq Llama 3.1, and multiple integrated tools for web research, calculations, and automated report generation.

The agent performs end-to-end company research and generates professional competitive intelligence reports in markdown format. It can compare two companies across funding, products, market position, strengths, weaknesses, recent news, and future outlook.

The system follows the ReAct (Reasoning + Acting) agent framework, allowing the AI to think step-by-step, use tools dynamically, and produce structured business analysis autonomously.

---

# Features

- Autonomous competitive analysis between two companies
- Real-time web research using DuckDuckGo Search
- Python execution for calculations and data comparison
- Automated markdown report generation
- ReAct-based reasoning workflow
- Groq-powered Llama 3.1 model integration
- Structured and professional business reports

---

# Tech Stack

- Python
- LangChain
- Groq API
- Llama 3.1 8B Instant
- DuckDuckGo Search
- Python REPL Tool

---

# Project Structure

```bash
.
├── main.py
├── .env
├── requirements.txt
└── competitive_analysis_*.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/rohn-negi/AI-Powered-Competitive-Intelligence-Agent-with-LangChain.git

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here

---

# Required Packages

```txt
langchain
langchain-groq
langchain-community
langchain-experimental
python-dotenv
duckduckgo-search
```

---

# Usage

Run the project:

```bash
python main.py
```

The application will ask for two company names:

```bash
Enter first company: 
Enter second company: 
```

The AI agent will then:

1. Research both companies
2. Gather market and funding information
3. Analyze products and services
4. Compare strengths and weaknesses
5. Generate a professional report
6. Save the report as a markdown file

---

# Example Analysis Sections

The generated report includes:

- Company Overview
- Funding and Valuation
- Products and Services
- Recent News
- Strengths and Weaknesses
- Head-to-Head Comparison
- Final Verdict

---

# How It Works

The project uses a LangChain ReAct Agent that combines reasoning with tool usage.

The agent has access to three primary tools:

### Web Search Tool
Used for researching companies, funding rounds, product launches, partnerships, and news.

### Python REPL Tool
Used for calculations, percentage comparisons, and numerical analysis.

### Save Report Tool
Stores the final competitive analysis report in markdown format.

The agent iteratively reasons through tasks, decides which tool to use, processes information, and generates the final report.

---

# Example Output


competitive_analysis_20260507_142530.md


