from pydantic import BaseModel


class Skill(BaseModel):
    name: str

    def __str__(self):
        return f"name: {self.name}"
