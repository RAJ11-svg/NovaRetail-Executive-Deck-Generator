from pptx import Presentation

ppt = Presentation(
    "template/novaretail_template.pptx"
)

for slide_num, slide in enumerate(
        ppt.slides,
        start=1):

    print(f"\n===== SLIDE {slide_num} =====")

    for shape in slide.shapes:

        print(
            f"Name: {shape.name}"
        )