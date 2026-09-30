from pydantic import BaseModel
from typing import List


class PromptRequest(BaseModel):
    story_prompt: str
    character_name: str
    setting: str
    tone: str
    art_style: str


class PanelOutline(BaseModel):
    panel_number: int
    title: str
    scene_description: str
    image_prompt: str


class OutlineResponse(BaseModel):
    panels: List[PanelOutline]


class ComicPanel(BaseModel):
    panel_number: int
    title: str
    scene_description: str
    dialogue: str = ""
    image_url: str = ""


class ComicResponse(BaseModel):
    title: str
    panels: List[ComicPanel]
    pdf_url: str