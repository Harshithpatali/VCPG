from backend.schemas.prompt_schema import PromptRequest

from backend.services.prompt_loader import (
    load_prompt
)

from backend.services.openrouter_service import (
    OpenRouterService
)


class OpenRouterAgent:

    def __init__(self):
        self.service = OpenRouterService()

    async def generate_blueprint(
        self,
        request: PromptRequest
    ) -> str:

        template = load_prompt(
            "architect_prompt.txt"
        )

        prompt = template.format(
            project_idea=request.project_idea,
            os=request.os,
            language=request.language,
            purpose=request.purpose,
            explanation=request.explanation,
            backend_deployment=request.backend_deployment,
            frontend_deployment=request.frontend_deployment
        )

        blueprint = await self.service.generate(
            prompt
        )

        return blueprint