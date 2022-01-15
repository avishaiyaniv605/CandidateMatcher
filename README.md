# CandidateMatcher

An application returning the best candidate for a given job.

The application is running on top of docker container. <br/>
In order to run the application, run the following commands: <br/>
- ```docker build -t fastapi-candidatematcher .```
- ```docker run -p 8000:8000 -t -i fastapi-candidatematcher```

**The server is now running in host ```localhost``` and listening to port ```8000```**

For your convenience, below is all the information you need in order to play/use the application:


### Models:

> **Job**
```{title: str, skills: List[Skill]}```

> **Skill**
```{name: str}```

> **Candidate**
```{id: Optional[int], title: str, skills: List[Skill]}```

### API:

| Request Type | Route                                    | Payload Payload | Response                            | Description                                           |
|--------------|------------------------------------------|-----------------|-------------------------------------|-------------------------------------------------------|
| **POST**     | **localhost:8000/candidates/match**      | **Job**         | **List[Candidate]**                 | **Return the candidates that best fit the given job** |
| POST         | localhost:8000/candidates/add            | List[Candidate] | dict[str, List[Candidate]]          | Add the given candidates to the DB                    |
| GET          | localhost:8000/candidates                | None            | List[Candidate]                     | Return the candidates stored in the DB                |
| GET          | localhost:8000/candidates/clean          | None            | str representing success or failure | Cleans all the candidates from the DB                 |
| GET          | localhost:8000/candidates/{candidate_id} | None            | str representing success or failure | Removes the candidate from the DB                     |
