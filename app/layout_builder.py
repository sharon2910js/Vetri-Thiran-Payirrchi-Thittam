def build_comic_layout(outline, story, image_urls):
    panels = []

    for index, panel in enumerate(outline.panels):
        dialogue = ""

        if index < len(story):
            dialogue = story[index].get("dialogue", "")

        image_url = ""

        if index < len(image_urls):
            image_url = image_urls[index]

        panels.append({
            "panel_number": panel.panel_number,
            "title": panel.title,
            "scene_description": panel.scene_description,
            "dialogue": dialogue,
            "image_url": image_url
        })

    return panels