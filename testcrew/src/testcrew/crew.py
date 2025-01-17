import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from .tools.custom_tool import StructuredDataQueryTool

# Load environment variables
load_dotenv()

class Testcrew(CrewBase):
    @agent
    def documentation_parser_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_parser_agent'],
            tools=[
                ScrapeWebsiteTool(website_url="https://documentation-using-ai-agent.readthedocs.io/en/latest/")
            ],
            llm={
                "provider": "gemini",
                "api_key": os.getenv("GEMINI_API_KEY"),
                "model": os.getenv("GEMINI_MODEL")
            },
            verbose=True
        )

    @agent
    def ui_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['UI_agent'],
            tools=[StructuredDataQueryTool()],
            llm={
                "provider": "gemini",
                "api_key": os.getenv("GEMINI_API_KEY"),
                "model": os.getenv("GEMINI_MODEL")
            },
            verbose=True
        )

    @task
    def process_documentation(self) -> Task:
        return Task(config=self.tasks_config['documentation_processing'])

    @task
    def handle_user_query(self) -> Task:
        return Task(config=self.tasks_config['query_processing'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
