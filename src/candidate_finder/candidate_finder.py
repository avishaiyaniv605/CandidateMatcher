from typing import List

from src.models.candidate import Candidate
from src.models.job import Job
import src.services.candidates_service as candidates_service


class CandidateMatchResult:
    def __init__(self, score: int, candidate: Candidate):
        self.candidate = candidate
        self.score = score


PERFECT_SCORE = 100
MEDIUM_SCORE = 60
LOW_SCORE = 20


def is_perfect_match(candidate: Candidate, job: Job):
    """
    :returns true if candidates title equals the job title and
    the candidate has the skill required for the job
    """
    is_title_match = candidate.title.lower() == job.title.lower()
    is_skill_match = job.skill.name.lower() in [sk.name.lower() for sk in candidate.skills]
    return is_title_match and is_skill_match


def is_medium_match(candidate: Candidate, job: Job):
    """
    :returns true if candidates title equals the job title and
    or the candidates title is included in the job title
    or the candidate has the needed skill for the job
    """
    is_title_match = candidate.title.lower() == job.title.lower()
    is_title_included = candidate.title.lower() in job.title.lower()
    is_skill_match = job.skill.name.lower() in [sk.name.lower() for sk in candidate.skills]
    return is_title_match or is_skill_match or is_title_included


def is_low_match(candidate: Candidate, job: Job):
    """
    :returns true if candidates title equals the job title and
    or the candidates title is included in the job title
    or part of the title is included
    or the candidate has the needed skill for the job
    """
    is_title_included = candidate.title.lower() in job.title.lower()

    job_title_parts = job.title.lower().split(" ")
    candidate_title_parts = candidate.title.lower().split(" ")
    is_part_of_title_included = False

    for job_title_part in job_title_parts:
        if job_title_part in candidate_title_parts:
            is_part_of_title_included = True

    is_skill_match = job.skill.name.lower() in [sk.name.lower() for sk in candidate.skills]
    return is_title_included or is_skill_match or is_part_of_title_included


def rate_match(candidate: Candidate, job: Job):
    if is_perfect_match(candidate, job):
        return CandidateMatchResult(PERFECT_SCORE, candidate)
    if is_medium_match(candidate, job):
        return CandidateMatchResult(MEDIUM_SCORE, candidate)
    if is_low_match(candidate, job):
        return CandidateMatchResult(LOW_SCORE, candidate)

    return CandidateMatchResult(0, candidate)


def find(job: Job) -> List[Candidate]:
    fetched_candidates = candidates_service.get_candidates()
    match_results = list(map(lambda cand: rate_match(cand, job), fetched_candidates))
    match_results = list(filter(lambda res: res.score > 0, match_results))
    match_results.sort(key=lambda e: e.score, reverse=True)
    return list(map(lambda res: res.candidate, match_results))
