from .calculator import Calculator
from .logger import get_logger, LoggingObserver, AutoSaveObserver
from .calculator_config import get_config

def create_calculator():
    config = get_config()
    logger = get_logger(config["log_file"])

    calc = Calculator()
    calc.add_observer(LoggingObserver(logger))
    if config["auto_save"]:
        calc.add_observer(AutoSaveObserver(config["history_file"]))
    return calc
