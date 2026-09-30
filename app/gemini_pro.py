from app.config import MOCK_AI


def generate_story(request, outline):

    if MOCK_AI:

        dialogues = [
            f"{request.character_name}: Wow! What is that?",
            f"{request.character_name}: Let's find out!",
            f"{request.character_name}: Wait! Did you hear that?",
            f"{request.character_name}: Don't worry, I have an idea!",
            f"{request.character_name}: We did it! What an adventure!"
        ]

        captions = [
            "A mysterious discovery begins.",
            "The adventure continues.",
            "Something unexpected appears.",
            "Our hero finds a clever solution.",
            "The adventure ends happily."
        ]

        narrations = [
            f"{request.character_name} discovers something strange in the {request.setting}.",
            f"{request.character_name} follows the mysterious clue.",
            f"A surprising challenge appears.",
            f"{request.character_name} bravely solves the problem.",
            f"{request.character_name} discovers the secret of the adventure."
        ]

        panels = []

        for i, panel in enumerate(outline.panels):

            panels.append({
                "panel_number": panel.panel_number,
                "caption": captions[i],
                "narration": narrations[i],
                "dialogue": dialogues[i]
            })

        return panels

    raise RuntimeError(
        "Real Gemini AI is not enabled. Set MOCK_AI=true for testing."
    )