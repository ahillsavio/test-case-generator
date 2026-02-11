from crewai import Crew, Process

from app.agents.requirement_analyst import create_requirement_analyst
from app.agents.test_designer import create_test_designer

from app.tasks.requirement_tasks import create_requirement_analysis_task
from app.tasks.test_design_tasks import create_test_design_task


def create_crew() -> Crew:
    # Create agents
    requirement_agent = create_requirement_analyst()
    test_agent = create_test_designer()

    # Create tasks with agents injected
    requirement_task = create_requirement_analysis_task(requirement_agent)
    test_task = create_test_design_task(test_agent)

    return Crew(
        agents=[requirement_agent, test_agent],
        tasks=[requirement_task, test_task],
        process=Process.sequential,
        verbose=True,
    )
