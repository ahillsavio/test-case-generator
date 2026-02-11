import logging
from pathlib import Path


def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=log_dir / "react_execution.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
