from crewai.tools import tool
import re
import json
from typing import Optional


@tool("Requirement Structuring Tool")
def requirement_parser_tool(agent_output: str) -> str:
    """
    Converts free-form agent reasoning into structured JSON.
    Extracts actor, action, object, conditions, and constraints.
    Deterministic. No LLM usage.
    """

    text = agent_output.strip()

    def extract(pattern: str) -> Optional[str]:
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    # Try labeled formats first
    actor = extract(r"actor\s*[:\-]\s*(.+)")
    action = extract(r"action\s*[:\-]\s*(.+)")
    obj = extract(r"object\s*[:\-]\s*(.+)")
    conditions = extract(r"(condition|when|if)\s*[:\-]?\s*(.+)")
    constraints = extract(r"(constraint|limit|range)\s*[:\-]?\s*(.+)")

    # Fallback heuristic parsing if labeled format not found
    if not actor:
        actor_match = re.search(r"the actor is\s+(.+)", text, re.IGNORECASE)
        actor = actor_match.group(1).strip() if actor_match else None

    if not action:
        action_match = re.search(r"the action is\s+(.+)", text, re.IGNORECASE)
        action = action_match.group(1).strip() if action_match else None

    if not conditions:
        condition_match = re.search(r"(when|if)\s+(.+)", text, re.IGNORECASE)
        conditions = condition_match.group(2).strip() if condition_match else None

    structured_output = {
        "actor": actor,
        "action": action,
        "object": obj,
        "conditions": conditions,
        "constraints": constraints,
        "original_analysis": text,
    }

    return json.dumps(structured_output, indent=2)
