import uvicorn
import src.services.candidates_service as candidates_service
from fastapi.logger import logger
from typing import List, Dict
from fastapi import FastAPI
from src.models.candidate import Candidate
from src.models.job import Job

app = FastAPI(debug=True)


@app.post("/candidates/match")
async def match_candidates_to_job(job: Job):
    """
    Given a job the application
    :returns the candidates that are most fit for the job sorted by their score
    """
    logger.error(f"About to get candidates for job: {job}")
    return candidates_service.match_candidates(job)


@app.get("/candidates")
async def list_candidates():
    logger.error(f"About to get all candidates")
    return candidates_service.get_candidates()


@app.post("/candidates/add")
async def add_candidates(candidates: List[Candidate]) -> dict[str, List[Candidate]]:
    """
    calling route /candidates/add with list of candidates will add
    the candidates to the db
    :return the updated list of candidates
    """
    logger.error(f"About to insert new candidates: {candidates}")
    candidates_service.insert_candidates(candidates)
    return {"updated_candidates": candidates_service.get_candidates()}


@app.get("/candidates/clean")
async def clean_candidates() -> str:
    """
    calling route /candidates/clean will clean all candidates from the db
    """
    logger.error("About to clean all candidates")
    candidates_service.clean_candidates()
    return "Cleaned successfully"


@app.delete("/candidates/{candidate_id}")
async def remove_candidate(candidate_id: int) -> str:
    """
    calling route /candidates/clean will remove candidate with received id
    """
    logger.error("About to clean all candidates")
    return candidates_service.remove_candidate(candidate_id)


if __name__ == '__main__':
    uvicorn.run(app)
