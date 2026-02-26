from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.llm import LLM
from typing import List

# define class for our crew
@CrewBase
class ResearchAndBlogCrew(): # class name same as project name

    agents: list[BaseAgent]
    task: list[Task]

    # define paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Define Ollama LLM once
    ollama_llm = LLM(
        model="ollama/llama3.2:3b",  # change to ollama/llama3.2:3b if you download it
        base_url="http://localhost:11434"
    )

    # Agents
    # Here, order does not matter
    @agent 
    def report_generator(self) -> Agent: # fn name same as agent name
        return Agent(
            config=self.agents_config["report_generator"],
            llm=self.ollama_llm  # 👈 add this

        )
    
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            llm=self.ollama_llm
        )

    # tasks
    # order of task definition matters
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"]
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="blogs/blog.md"
        )

    # crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )