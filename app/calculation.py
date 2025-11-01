from dataclasses import dataclass
from datetime import datetime

@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float
    timestamp: str | None = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            operation=data["operation"],
            a=float(data["a"]),
            b=float(data["b"]),
            result=float(data["result"]),
            timestamp=data.get("timestamp"),
        )
