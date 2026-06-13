import httpx

from backend.config import settings


class OpenRouterService:

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    async def generate(
        self,
        prompt: str
    ) -> str:

        headers = {
            "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        async with httpx.AsyncClient(
            timeout=120
        ) as client:

            response = await client.post(
                self.BASE_URL,
                headers=headers,
                json=payload
            )

            response.raise_for_status()

            data = response.json()

            return (
                data["choices"][0]
                ["message"]
                ["content"]
            )