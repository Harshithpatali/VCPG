from fastapi import (
    APIRouter,
    HTTPException
)

from backend.schemas.prompt_schema import (
    PromptRequest,
    PromptResponse
)

from backend.agents.orchestrator import (
    PromptOrchestrator
)

router = APIRouter()

orchestrator = PromptOrchestrator()


@router.post(
    "/generate-prompt",
    response_model=PromptResponse
)
async def generate_prompt(
    request: PromptRequest
):
    try:

        final_prompt = await (
            orchestrator.generate_prompt(
                request
            )
        )

        return PromptResponse(
            success=True,
            final_prompt=final_prompt
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )