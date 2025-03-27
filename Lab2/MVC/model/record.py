from dataclasses import dataclass

@dataclass
class Record:
    fio: str
    composition: str
    position: str
    titles: int
    sport_type: str
    rank: str