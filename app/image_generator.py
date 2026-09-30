from pathlib import Path
import os

from huggingface_hub import InferenceClient


def generate_image(
    prompt: str,
    panel_number: int
) -> str:

    output_dir = Path("generated/images")
    output_dir.mkdir(parents=True, exist_ok=True)

    image_path = output_dir / f"panel_{panel_number}.png"

    token = os.getenv("HF_TOKEN")

    if not token:
        raise RuntimeError(
            "HF_TOKEN is not set. Add your Hugging Face token to .env"
        )

    client = InferenceClient(
        provider="hf-inference",
        api_key=token
    )

    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    image.save(image_path)

    return f"/generated/images/{image_path.name}"