import httpx

from backend.config import settings


class GroqService:

    BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

    async def generate(
        self,
        prompt: str
    ) -> str:

        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3
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