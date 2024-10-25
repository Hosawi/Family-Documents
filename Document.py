# info. 
# 'notes' member varible is deleted 
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Document:
    id: str
    title: str
    description: str
    classification: str
    file_path: str
    upload_date: str

    @classmethod
    def get_fields(cls) -> List[str]:
        return list(cls.__annotations__.keys())

    def to_dict(self):
        return asdict(self)
