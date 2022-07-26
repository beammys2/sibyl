from pydantic import BaseModel


class WikiAgentRequest(BaseModel):
    model_source: str
    model_type: str
    query: str
    model_name: str | None = None
    agent_type: str


class WikiAgentResponse(BaseModel):
    status: str
    data: str


class VectorStoreStatusResponse(BaseModel):
    embeddings_db: str
