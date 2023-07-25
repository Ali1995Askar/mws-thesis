from dataclasses import dataclass
from typing import Tuple


@dataclass
class Edge:
    worker_id: str
    task_id: str

    def as_tuple(self) -> Tuple[str, str]:
        return self.worker_id, self.task_id
