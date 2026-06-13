from pydantic import BaseModel


class PromptRequest(BaseModel):
    project_idea: str
    os: str
    language: str
    purpose: str
    explanation: bool
    backend_deployment: str
    frontend_deployment: str


class PromptResponse(BaseModel):
    success: bool
    final_prompt: str