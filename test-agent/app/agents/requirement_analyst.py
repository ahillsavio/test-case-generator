from crewai import Agent
from app.llm.provider import get_llm
from app.tools.requirement_parser import requirement_parser_tool


def create_requirement_analyst() -> Agent:
    llm = get_llm()

    return Agent(
        role="Requirement Analyst",
        goal=(
            "Analyze a software requirement and extract its structured components."
        ),
        backstory=(
            "You are a senior QA analyst skilled at breaking down requirements "
            "into precise and testable components.\n\n"
            "You MUST follow this exact format when presenting your analysis:\n\n"
            "Actor: <identified actor>\n"
            "Action: <identified action>\n"
            "Object: <identified object>\n"
            "Conditions: <identified conditions or None>\n"
            "Constraints: <identified constraints or None>\n\n"
            "Do not provide explanations.\n"
            "Do not provide commentary.\n"
            "Only output the labeled fields exactly as shown above.\n\n"
            "After producing this labeled output, use the available tool to "
            "convert it into structured JSON and return that JSON as the final answer.\n"
            "Once JSON is returned, stop."
        ),
        tools=[requirement_parser_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
