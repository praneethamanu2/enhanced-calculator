import logging
import pandas as pd

def get_logger(log_file):
    logger = logging.getLogger("calculator")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger

class Observer:
    def update(self, calculation, history):  # pragma: no cover
        pass

class LoggingObserver(Observer):
    def __init__(self, logger):
        self.logger = logger

    def update(self, calculation, history):
        self.logger.info(
            "Calc: %s(%s, %s) = %s",
            calculation.operation,
            calculation.a,
            calculation.b,
            calculation.result,
        )

class AutoSaveObserver(Observer):
    def __init__(self, history_file):
        self.history_file = history_file

    def update(self, calculation, history):
        df = pd.DataFrame([c.to_dict() for c in history])
        df.to_csv(self.history_file, index=False)
