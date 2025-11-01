import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

def get_config():
    log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
    history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "history")
    max_history = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
    auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "false").lower() == "true"
    precision = int(os.getenv("CALCULATOR_PRECISION", "4"))
    max_input = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e9"))
    encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

    (BASE_DIR / log_dir).mkdir(parents=True, exist_ok=True)
    (BASE_DIR / history_dir).mkdir(parents=True, exist_ok=True)

    return {
        "log_dir": BASE_DIR / log_dir,
        "history_dir": BASE_DIR / history_dir,
        "max_history": max_history,
        "auto_save": auto_save,
        "precision": precision,
        "max_input": max_input,
        "encoding": encoding,
        "history_file": (BASE_DIR / history_dir / "history.csv"),
        "log_file": (BASE_DIR / log_dir / "calculator.log"),
    }
