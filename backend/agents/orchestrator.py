from backend.schemas.prompt_schema import (
    PromptRequest
)

from backend.agents.openrouter_agent import (
    OpenRouterAgent
)

from backend.agents.groq_agent import (
    GroqAgent
)


class PromptOrchestrator:

    def __init__(self):

        self.openrouter_agent = (
            OpenRouterAgent()
        )

        self.groq_agent = (
            GroqAgent()
        )

    async def generate_prompt(
        self,
        request: PromptRequest
    ) -> str:

        blueprint = await (
            self.openrouter_agent
            .generate_blueprint(
                request
            )
        )

        final_prompt = await (
            self.groq_agent
            .refine_blueprint(
                blueprint
            )
        )

        return final_prompt