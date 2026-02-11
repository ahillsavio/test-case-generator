import logging
from app.crew.crew import create_crew
from app.utils.logger import setup_logging
from dotenv import load_dotenv
import litellm

load_dotenv()


def run(requirement: str) -> str:
    # litellm.add_default_params = {"tool_choice": "none"}
    
    crew = create_crew()

    logging.info("Starting Crew Execution")
    logging.info(f"Input Requirement: {requirement}")

    result = crew.kickoff(
        inputs={"requirement": requirement}
    )

    logging.info("Crew Execution Finished")
    logging.info(f"Final Output:\n{result}")

    return str(result)


if __name__ == "__main__":
    setup_logging()

    try:
        user_requirement = input("Enter the software requirement:\n\n")

        if not user_requirement.strip():
            raise ValueError("Requirement cannot be empty.")

        final_output = run(user_requirement)

        print("\n\n========== FINAL OUTPUT ==========\n")
        print(final_output)

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"\nError occurred: {e}")
