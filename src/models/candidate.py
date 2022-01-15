from typing import List
from pydantic import BaseModel
from src.models.skill import Skill


class Candidate(BaseModel):
    id: int | None = None
    title: str
    skills: List[Skill]

    def __str__(self):
        return f"| title: {self.title}, skills: {[skill.__str__() for skill in self.skills]} |"