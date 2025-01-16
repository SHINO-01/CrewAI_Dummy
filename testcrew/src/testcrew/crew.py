import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, da

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

@CrewBase
class Testcrew:
    @agent
    def documentation_parser_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_parser_agent'],
            tools=[
                ScrapeWebsiteTool(website_url="https://your-docs.readthedocs.io")
            ],
            llm={
                "provider": "groq",
                "api_key": GROQ_API_KEY,
                "model": GROQ_MODEL
            },
            verbose=True
        )

    @agent
    def ui_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['UI_agent'],
            tools=[QueryStructuredDataTool()],
            llm={
                "provider": "groq",
                "api_key": GROQ_API_KEY,
                "model": GROQ_MODEL
            },
            verbose=True
        )

    @agent
    def knowledge_synth_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Knowledge_synth_agent'],
            llm={
                "provider": "groq",
                "api_key": GROQ_API_KEY,
                "model": GROQ_MODEL
            },
            verbose=True
        )

    @agent
    def solution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['solution_agent'],
            llm={
                "provider": "groq",
                "api_key": GROQ_API_KEY,
                "model": GROQ_MODEL
            },
            verbose=True
        )

    @task
    def process_documentation(self) -> Task:
        return Task(config=self.tasks_config['process_documentation'])

    @task
    def handle_user_query(self) -> Task:
        return Task(config=self.tasks_config['handle_user_query'])

    @task
    def synthesize_knowledge(self) -> Task:
        return Task(config=self.tasks_config['synthesize_knowledge'])

    @task
    def generate_solution(self) -> Task:
        return Task(config=self.tasks_config['generate_solution'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
