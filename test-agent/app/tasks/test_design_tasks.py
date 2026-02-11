from crewai import Task
from crewai import Agent


def create_test_design_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Using the structured requirement below:\n\n"
            "{requirement_analysis_task.output}\n\n"
            "Design comprehensive test cases including:\n"
            "- Positive scenarios\n"
            "- Negative scenarios\n\n"
            "Each test case must clearly include:\n"
            "Title\n"
            "Preconditions\n"
            "Steps (numbered)\n"
            "Expected Result\n"
        ),
        expected_output=(
            "Strict JSON structured test cases that cover both positive and negative scenarios."
        ),
        agent=agent,
    )
