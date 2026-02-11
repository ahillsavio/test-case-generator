from crewai import Task
from crewai import Agent


def create_requirement_analysis_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Analyze the following software requirement:\n\n"
            "{requirement}\n\n"
            "Break it down clearly into:\n"
            "- Actor\n"
            "- Action\n"
            "- Object\n"
            "- Conditions\n"
            "- Constraints\n\n"
            "Clearly label each element."
        ),
        expected_output=(
            "A STRICT JSON object with the following keys:\n"
            "actor, action, object, conditions, constraints.\n\n"
            "The output MUST be valid JSON."
        ),
        agent=agent,
    )

