from crewai import Agent
from app.llm.provider import get_llm
from app.tools.formatter import formatter_tool


def create_test_designer() -> Agent:
    llm = get_llm()
    
    return Agent(
        role="QA Test Designer",
        goal=(
            "Design high-quality positive and negative test cases "
            "based on a structured software requirement."
        ),
        backstory=(
            "You are a senior QA engineer specializing in functional test design.\n\n"
            "You carefully analyze structured requirement details and design "
            "clear, executable test cases.\n\n"
            "IMPORTANT RULES:\n"
            "• Generate a MAXIMUM of 5 test cases.\n"
            "• Generate at least 3 test cases if possible.\n"
            "• Include both positive and negative scenarios.\n"
            "• Do NOT exceed 5 test cases under any circumstance.\n\n"
            "Each test case MUST include:\n"
            "- Title\n"
            "- Preconditions\n"
            "- Steps (numbered)\n"
            "- Expected Result\n\n"
            "After generating the test cases, use the formatter tool "
            "to convert the output into structured JSON.\n"
            "Call the tool only once and return its output as final answer."
        ),
        tools=[formatter_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
