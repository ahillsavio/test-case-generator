from crewai.tools import tool
import re
import json
from typing import List, Dict


@tool("Test Case Formatter Tool")
def formatter_tool(test_cases_text: str) -> str:
    """
    Converts free-form test case text into structured JSON.
    Deterministic parsing only. No LLM usage.
    """

    text = test_cases_text.strip()

    # Split into individual test cases
    test_case_blocks = re.split(r"Test Case \d+:", text, flags=re.IGNORECASE)

    structured_cases: List[Dict] = []

    for block in test_case_blocks:
        block = block.strip()
        if not block:
            continue

        title_match = re.search(r"Title:\s*(.+)", block, re.IGNORECASE)
        preconditions_match = re.search(r"Preconditions:\s*(.+)", block, re.IGNORECASE)
        expected_match = re.search(r"Expected Result:\s*(.+)", block, re.IGNORECASE)

        steps_match = re.search(
            r"Steps:\s*((?:.|\n)*?)(?:Expected Result:|$)",
            block,
            re.IGNORECASE,
        )

        steps_list = []
        if steps_match:
            steps_text = steps_match.group(1).strip()
            steps = re.findall(r"\d+\.\s*(.+)", steps_text)
            steps_list = [step.strip() for step in steps]

        structured_cases.append(
            {
                "title": title_match.group(1).strip() if title_match else None,
                "preconditions": preconditions_match.group(1).strip()
                if preconditions_match
                else None,
                "steps": steps_list,
                "expected_result": expected_match.group(1).strip()
                if expected_match
                else None,
            }
        )

    return json.dumps(structured_cases, indent=2)
