from backend.services.prompt_loader import (
    load_prompt
)

from backend.services.groq_service import (
    GroqService
)


class GroqAgent:

    def __init__(self):
        self.service = GroqService()

    async def refine_blueprint(
        self,
        blueprint: str
    ) -> str:

        template = load_prompt(
            "refinement_prompt.txt"
        )

        prompt = template.format(
            blueprint=blueprint
        )

        refined_prompt = await (
            self.service.generate(prompt)
        )

        return refined_prompt