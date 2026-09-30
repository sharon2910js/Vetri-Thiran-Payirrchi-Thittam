from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf


def generate_comic(request):

    outline = generate_outline(request)

    story = generate_story(
        request,
        outline
    )

    image_urls = []

    for panel in outline.panels:
        image_url = generate_image(
            prompt=panel.image_prompt,
            panel_number=panel.panel_number
        )
        image_urls.append(image_url)

    panels = build_comic_layout(
        outline,
        story,
        image_urls
    )

    title = f"{request.character_name}'s Comic"

    pdf_url = save_pdf(
        title,
        panels
    )

    return {
        "title": title,
        "panels": panels,
        "pdf_url": pdf_url
    }