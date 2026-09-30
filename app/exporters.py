from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)


def save_pdf(title, panels):

    output_dir = Path("generated")
    output_dir.mkdir(exist_ok=True)

    safe_title = "".join(
        c if c.isalnum() or c in " _-" else "_"
        for c in title
    )

    pdf_path = output_dir / f"{safe_title}.pdf"

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(title, styles["Title"])
    )

    story.append(Spacer(1, 20))

    for panel in panels:

        story.append(
            Paragraph(
                f"Panel {panel['panel_number']}: {panel['title']}",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 10))

        image_url = panel.get("image_url")

        if image_url:
            image_path = Path(
                image_url.lstrip("/").replace("/", "\\")
            )

            if image_path.exists():
                img = Image(
                    str(image_path),
                    width=450,
                    height=280
                )
                story.append(img)
                story.append(Spacer(1, 10))

        story.append(
            Paragraph(
                panel.get("scene_description", ""),
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 10))

        dialogue = panel.get("dialogue", "")

        if dialogue:
            story.append(
                Paragraph(
                    f"<b>Dialogue:</b> {dialogue}",
                    styles["BodyText"]
                )
            )

        story.append(Spacer(1, 25))

    doc.build(story)

    return f"/generated/{pdf_path.name}"