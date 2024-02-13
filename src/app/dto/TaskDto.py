from dataclasses import dataclass, field
from typing import List
from marshmallow_dataclass import class_schema
from marshmallow import EXCLUDE, Schema


@dataclass
class Label:
    color: str

    class Meta:
        unknown = EXCLUDE


@dataclass
class Tag:
    text: str

    class Meta:
        unknown = EXCLUDE


@dataclass
class Task:
    id: int
    item: str
    image: str = ""
    labels: List[Label] = field(default_factory=list)
    tags: List[Tag] = field(default_factory=list)

    class Meta:
        unknown = EXCLUDE


@dataclass
class CardList:
    id: int
    title: str
    cards: List[Task]

    class Meta:
        unknown = EXCLUDE


card_list_schema = class_schema(CardList)(many=True)
