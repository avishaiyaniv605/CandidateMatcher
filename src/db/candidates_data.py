from typing import List

from src.models.candidate import Candidate
from src.models.skill import Skill

candidates_raw = [
    {
        "title": "Software Engineer",
        "skills": ["Java", "Spring", "Python", "C#", "API", "Microservices", "Docker", "Kubernetes"]
    },
    {
        "title": "Software Engineer",
        "skills": ["Python", "Microservices", "Backend", "Deep Learning", "Docker"]
    },
    {
        "title": "Data Scientist",
        "skills": ["Python", "Jupiter", "Backend", "Deep Learning", "NLP"]
    },
    {
        "title": "Support Engineer",
        "skills": []
    },
    {
        "title": "UX Designer",
        "skills": ["Photoshop", "Indesign", "Paint"]
    },
    {
        "title": "Talent Acquisition Specialist",
        "skills": ["Human Resources", "Recruiting"]
    },
    {
        "title": "Automation Engineer",
        "skills": ["Selenium", "TestNG", "Java"]
    },
    {
        "title": "BI Developer",
        "skills": ["Big Data", "Hadoop"]
    },
    {
        "title": "Automation Engineer",
        "skills": ["Selenium", "Specflow", "C#", "BDD", "xUnit"]
    },
    {
        "title": "Automation Engineer",
        "skills": ["Selenium", "Specflow", "C#", "BDD", "xUnit", "Nunit", "MsTest"]
    },
    {
        "title": "BI Developer",
        "skills": ["Big Data", "Hadoop", "Kafka", "Python"]
    },
    {
        "title": "Software Developer",
        "skills": ["Scala", "Hadoop", "Kafka", "Python"]
    }
]


def build_candidate(candidate_id: int, title: str, raw_skills: List[str]):
    skills = [Skill(name=sk) for sk in raw_skills]
    return Candidate(id=candidate_id, title=title, skills=skills)


candidates_sample = [build_candidate(i + 1, cr.get("title"), cr.get("skills")) for (i, cr) in enumerate(candidates_raw)]
