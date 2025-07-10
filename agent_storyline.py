import os
import logging
from openai import AsyncOpenAI

class StorylineAgent:
    """
    A self-contained agent responsible for generating a game storyline.
    Its logic is completely separate from the workflow engine.
    """
    def __init__(self):
        if not os.environ.get("OPENAI_API_KEY"):
            raise ValueError("The OPENAI_API_KEY environment variable is not set.")
        self.client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.prompt_text = """
We need simple common well-played game ideas. Single player preferred, but surprise me sometimes with 2+ player ones.
The game must be a known one so the rules should well understood, maybe clarify any variation of the game rules.
Name the game, describe the setting, the vibe, the atmosphere. If applicable give use a touch of the protagonist/antagonist, heroine, challenge, gear etc. Would be nice if the actual player could have a connection with the goals of the game.  
Generate a short one paragraph idea that outlines such a game! Include everything needed for a crisp requirement. Do not go into technologies or technical analysis, no integration. Focus on the core idea of a popular game.
(Each idea will be fed to ai code generators which produce poc mini games. Keep it simple. Because this is in an agentic workflow: use your powers to pass necessary specifications to image generating and source code generating agent.)
"""

    async def generate(self):
        """
        This is the core logic method. It is called by the workflow task.
        It interacts with the OpenAI API and prints the result.
        """
        logging.info("StorylineAgent is generating a storyline.")
        try:
            logging.info("Sending prompt to OpenAI...")
            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": self.prompt_text}]
            )
            storyline = response.choices[0].message.content
            logging.info("Successfully generated storyline.")
            print(f"--- AGENT RESULT ---\n{storyline}")
            return storyline
        except Exception as e:
            logging.error(f"An error occurred while calling OpenAI: {e}")
            print(f"--- AGENT ERROR ---\n{e}")
