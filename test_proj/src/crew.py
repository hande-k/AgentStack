from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import agentstack

@CrewBase
class TestprojCrew():
    """test_proj crew"""

    # Agent definitions
    @agent
    def alex(self) -> Agent:
        return Agent(
            config=self.agents_config['alex'],
            tools=[*agentstack.tools['file_read']],  # Pass in what tools this agent should have
            verbose=True,
            
        )

    # Task definitions
    @task
    def hello_world(self) -> Task:
        return Task(
            config=self.tasks_config['hello_world'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )