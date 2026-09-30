from google import genai
from google.genai import types

from app.config import (
    GEMINI_API_KEY,
    GEMINI_OUTLINE_MODEL,
    MOCK_AI
)

from app.schemas import (
    OutlineResponse,
    PanelOutline,
    PromptRequest
)


# =========================================================
# GEMINI CLIENT
# =========================================================

def get_client():

    if not GEMINI_API_KEY:

        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Add it to .env or set MOCK_AI=true."
        )

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


# =========================================================
# MOCK OUTLINE
# =========================================================

def generate_mock_outline(
    request: PromptRequest
) -> OutlineResponse:

    panels = []

    for number in range(1, 6):

        panels.append(

            PanelOutline(

                panel_number=number,

                title=f"Panel {number}",

                scene_description=(
                    f"{request.character_name} "
                    f"is exploring the "
                    f"{request.setting}."
                ),

                image_prompt=(
                    f"{request.art_style} comic illustration, "
                    f"{request.character_name} in "
                    f"{request.setting}, "
                    f"scene {number}, "
                    f"{request.tone} mood, "
                    "cinematic composition, "
                    "expressive character, "
                    "consistent character design"
                )
            )
        )

    return OutlineResponse(
        panels=panels
    )


# =========================================================
# REAL GEMINI OUTLINE
# =========================================================

def generate_outline(
    request: PromptRequest
) -> OutlineResponse:

    if MOCK_AI:

        return generate_mock_outline(
            request
        )


    client = get_client()


    prompt = f"""
You are an expert comic book story planner.

Create a cohesive 5-panel comic outline.

USER STORY:
{request.story_prompt}

MAIN CHARACTER:
{request.character_name}

SETTING:
{request.setting}

TONE:
{request.tone}

ART STYLE:
{request.art_style}

STRICT REQUIREMENTS:

1. Return exactly 5 panels.
2. Panel 1 introduces the situation.
3. Panels 2 and 3 develop the story.
4. Panel 4 creates the main turning point.
5. Panel 5 provides a satisfying ending.
6. Keep the same main character throughout.
7. Keep visual continuity.
8. Every panel needs an image prompt.
9. Do not put speech text inside image prompts.
10. Image prompts must describe visual content.
"""


    response = client.models.generate_content(

        model=GEMINI_OUTLINE_MODEL,

        contents=prompt,

        config=types.GenerateContentConfig(

            temperature=0.9,

            response_mime_type="application/json",

            response_schema=OutlineResponse
        )
    )


    return OutlineResponse.model_validate_json(
        response.text
    )