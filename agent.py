from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from datetime import datetime

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)


search = DuckDuckGoSearchRun()
python_repl = PythonREPLTool()

def save_report(content: str) -> str:
    filename = f"competitive_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Report saved to {filename}"

tools = [
    Tool(
        name="web_search",
        func=search.run,
        description="Search the internet for company information, news, funding, products, revenue, and market data. Use this for researching any company."
    ),
    Tool(
        name="python_repl",
        func=python_repl.run,
        description="Execute Python code for calculations and data processing. Use this to compare numbers, calculate percentages, or process any data."
    ),
    Tool(
        name="save_report",
        func=save_report,
        description="Save the final competitive analysis report in markdown format. Use this as the LAST step after all research is complete. Input should be the complete formatted report."
    )
]


prompt = PromptTemplate.from_template("""You are an expert business analyst specializing in competitive intelligence.
Your job is to research companies thoroughly and produce professional analysis reports.
Always be factual, cite specific numbers when available, and provide actionable insights.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}""")


agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=20,
    handle_parsing_errors=True
)


company1 = input("Enter first company: ")
company2 = input("Enter second company: ")

result = agent_executor.invoke({
    "input": f"""Conduct a comprehensive competitive analysis of {company1} vs {company2}.

Research and cover ALL of the following:

1. COMPANY OVERVIEW
   - What does each company do?
   - When were they founded?
   - Where are they headquartered?

2. FUNDING & VALUATION
   - Total funding raised
   - Latest valuation
   - Key investors

3. PRODUCTS & SERVICES
   - Core products
   - Key features
   - Target market

4. RECENT NEWS
   - Latest developments
   - Recent partnerships or acquisitions
   - Any controversies

5. STRENGTHS & WEAKNESSES
   - What each company does well
   - Where each company struggles

6. HEAD TO HEAD COMPARISON
   - Side by side metrics where possible
   - Use python_repl to calculate any comparisons

7. FINAL VERDICT
   - Which company has stronger market position?
   - Which is better positioned for the future?

After completing all research, save the complete report as a markdown file using save_report tool.
Format the report professionally with clear headers and sections."""
})


print("ANALYSIS COMPLETE")
print(result["output"])