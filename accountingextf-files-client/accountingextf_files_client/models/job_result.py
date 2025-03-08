from enum import Enum

class JobResult(str, Enum):
    FAILED = "failed"
    PENDING = "pending"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
