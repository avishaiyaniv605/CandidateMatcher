from typing import List

import src.candidate_finder.candidate_finder as candidate_finder
from src.db.candidates_data import candidates_sample
from src.models.candidate import Candidate
from src.models.job import Job


candidate_id_pk: int = candidates_sample[len(candidates_sample) - 1].id + 1
candidatesTable = candidates_sample


def get_candidates():
    return candidatesTable


def insert_candidate(candidate: Candidate):
    global candidate_id_pk

    new_candidate = Candidate(**candidate.dict())
    new_candidate.id = candidate_id_pk
    candidatesTable.append(new_candidate)
    candidate_id_pk += 1


def insert_candidates(candidates: List[Candidate]):
    for can in candidates:
        insert_candidate(can)


def clean_candidates():
    candidatesTable.clear()


def remove_candidate(candidate_id: int):
    global candidatesTable

    len_without_candidate = len(list(filter(lambda c: c.id != candidate_id, candidatesTable)))

    if len_without_candidate == len(candidatesTable):
        return "Candidate not found!"
    else:
        candidatesTable = list(filter(lambda c_id: c_id != candidate_id, candidatesTable))
        return "Removed successfully!"


def match_candidates(job: Job):
    return candidate_finder.find(job)



