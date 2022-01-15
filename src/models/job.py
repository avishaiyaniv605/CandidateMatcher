from pydantic import BaseModel
from src.models.skill import Skill


class Job(BaseModel):
    title: str
    skill: Skill

    def __str__(self):
        return f"| title: {self.title}, skill: {self.skill} |"
