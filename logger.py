import logging
from pathlib import Path

# Create logs directory if it doesn't exist
log_directory = Path("logs")
log_directory.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    handlers=[
        logging.FileHandler(log_directory / "bank.log"),
        logging.StreamHandler()  # Also print logs to console
    ]
)

logger = logging.getLogger(__name__)