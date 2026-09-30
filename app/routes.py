import traceback

from fastapi import (
    APIRouter,
    Form,
    HTTPException,
    Request
)

from fastapi.responses import HTMLResponse

from fastapi.templating import (
    Jinja2Templates
)

from app.config import TEMPLATES_DIR

from app.image_generator import (
    generate_image
)

from app.schemas import (
    PromptRequest
)

from app.services import (
    generate_comic
)


# =========================================================
# ROUTER
# =========================================================

router = APIRouter()


# =========================================================
# TEMPLATES
# =========================================================

templates = Jinja2Templates(

    directory=str(
        TEMPLATES_DIR
    )
)


# =========================================================
# HOME
# =========================================================

@router.get(
    "/",
    response_class=HTMLResponse
)
async def home(
    request: Request
):

    return templates.TemplateResponse(

        request=request,

        name="index.html",

        context={}
    )


# =========================================================
# GENERATE COMIC - FORM
# =========================================================

@router.post(
    "/generate",
    response_class=HTMLResponse
)
async def generate(

    request: Request,

    story_prompt: str = Form(...),

    character_name: str = Form(...),

    setting: str = Form(...),

    tone: str = Form(...),

    art_style: str = Form(...)

):

    try:

        data = PromptRequest(

            story_prompt=story_prompt,

            character_name=character_name,

            setting=setting,

            tone=tone,

            art_style=art_style
        )


        comic = generate_comic(
            data
        )


        return templates.TemplateResponse(

            request=request,

            name="comic_preview.html",

            context={
                "comic": comic
            }
        )


    except Exception as error:

        traceback.print_exc()


        return templates.TemplateResponse(

            request=request,

            name="error.html",

            context={
                "error": str(error)
            },

            status_code=500
        )


# =========================================================
# GENERATE COMIC - JSON API
# =========================================================

@router.post(
    "/generate-comic/json"
)
async def generate_comic_api(

    payload: PromptRequest

):

    try:

        return generate_comic(
            payload
        )


    except Exception as error:

        traceback.print_exc()


        raise HTTPException(

            status_code=500,

            detail=str(error)
        ) from error


# =========================================================
# IMAGE TEST
# =========================================================

@router.post(
    "/test-image"
)
async def test_image(

    prompt: str = Form(...)

):

    try:

        image_url = generate_image(

            prompt=prompt,

            panel_number=0
        )


        return {
            "image_url": image_url
        }


    except Exception as error:

        raise HTTPException(

            status_code=500,

            detail=str(error)
        ) from error


# =========================================================
# EXPORT SUCCESS
# =========================================================

@router.get(
    "/export-success",
    response_class=HTMLResponse
)
async def export_success(

    request: Request,

    pdf_url: str = ""
):

    return templates.TemplateResponse(

        request=request,

        name="export_success.html",

        context={
            "pdf_url": pdf_url
        }
    )