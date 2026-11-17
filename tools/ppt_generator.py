from pptx.dml.color import RGBColor
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN
from pptx import Presentation
from tools.business_story import generate_story
from google.adk.tools import ToolContext

def format_text(
    shape,
    color=(255, 255, 255),
    size=12,
    bold=False,
    italic=False,
    align=PP_ALIGN.LEFT
):
    if not shape.has_text_frame:
        return

    for paragraph in shape.text_frame.paragraphs:
        paragraph.alignment = align

        for run in paragraph.runs:
            run.font.color.rgb = RGBColor(
                color[0],
                color[1],
                color[2]
            )

            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.italic = italic


def generate_executive_ppt(tool_context: ToolContext) -> dict:
    """Generate the NovaRetail executive deck and update session state."""

    story = tool_context.state.get("business_story")
    if not story:
        story = generate_story()
        tool_context.state["business_story"] = story

    ppt = Presentation(
        "template/novaretail_template.pptx"
    )

    slide1 = ppt.slides[0]

    for shape in slide1.shapes:

        if shape.name == "deck_title":

            shape.text = "NovaRetail - Quarterly Business Review"

            format_text(
                shape,
                color=(255, 255, 255),
                size=34,
                bold=True
            )

        elif shape.name == "subtitle_1":

            shape.text = "Q2 2026 - Executive Review"

            format_text(
                shape,
                color=(202, 220, 252),
                size=18,
                bold=False
            )

        elif shape.name == "kpi1_value":

            shape.text = story["total_revenue_display"]

            format_text(
                shape,
                color=(255, 255, 255),
                size=30,
                bold=True,
                align=PP_ALIGN.CENTER
            )

        elif shape.name == "kpi1_label":

            shape.text = "Total Revenue"

            format_text(
                shape,
                color=(255, 255, 255),
                size=18,
                bold=False,
                align=PP_ALIGN.CENTER
            )

        elif shape.name == "kpi2_value":

            shape.text = str(story["avg_nps"])

            format_text(
                shape,
                color=(255, 255, 255),
                size=30,
                bold=True,
                align=PP_ALIGN.CENTER
            )

        elif shape.name == "kpi2_label":

            shape.text = "Average NPS"

            format_text(
                shape,
                color=(255, 255, 255),
                size=18,
                bold=False,
                align=PP_ALIGN.CENTER
            )

        elif shape.name == "kpi3_value":

            shape.text = f"{story['highest_stockout_rate']}%"

            format_text(
                shape,
                color=(255, 255, 255),
                size=30,
                bold=True,
                align=PP_ALIGN.CENTER
            )

        elif shape.name == "kpi3_label":

            shape.text = "Highest Stockout Rate"

            format_text(
                shape,
                color=(255, 255, 255),
                size=18,
                bold=False,
                align=PP_ALIGN.CENTER
            )

        elif shape.name == "summary_text":

            shape.text = (
                f"{story['best_region']} remains the strongest revenue contributor, while "
                f"{story['top_nps_region']} leads customer satisfaction performance. "
                f"{story['highest_risk_region']} continues to represent the largest operational risk area. "
                f"Management should balance growth investments with focused risk mitigation efforts."
            )

            format_text(
                shape,
                color=(255, 255, 255),
                size=16,
                bold=False,
                italic=True
            )

    for shape in list(slide1.shapes):

        if shape.name == "icon_1":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide1.shapes.add_picture(
                "icons/globe_region.png",
                left,
                top,
                width,
                height
            )

    slide2 = ppt.slides[1]

    for shape in list(slide2.shapes):

        if shape.name == "title_2":

            shape.text = story["slide2_title"]

            format_text(
                shape,
                color=(30, 39, 97),
                size=26,
                bold=True
            )

        elif shape.name == "insights_performance":

            shape.text = story["performance_insights"]

            format_text(
                shape,
                color=(30, 39, 97),
                size=18,
                bold=False
            )

        elif shape.name == "chart_performance":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide2.shapes.add_picture(
                "charts/revenue_chart.png",
                left,
                top,
                width,
                height
            )

        elif shape.name == "icon_2":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide2.shapes.add_picture(
                "icons/growth_chart.png",
                left + width * 0.1,
                top + height * 0.1,
                width,
                height * 1.2
            )

    slide3 = ppt.slides[2]

    for shape in list(slide3.shapes):

        if shape.name == "title_3":

            shape.text = story["slide3_title"]

            format_text(
                shape,
                color=(30, 39, 97),
                size=26,
                bold=True
            )

        elif shape.name == "insights_customer":

            shape.text = story["customer_insights"]

            format_text(
                shape,
                color=(30, 39, 97),
                size=18,
                bold=False
            )

        elif shape.name == "chart_customer":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide3.shapes.add_picture(
                "charts/customer_chart.png",
                left,
                top,
                width,
                height
            )

        elif shape.name == "icon_3":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide3.shapes.add_picture(
                "icons/customer_star.png",
                left + width * 0.1,
                top + height * 0.1,
                width,
                height * 1.2
            )

    slide4 = ppt.slides[3]

    for shape in list(slide4.shapes):

        if shape.name == "title_4":

            shape.text = story["slide4_title"]

            format_text(
                shape,
                color=(30, 39, 97),
                size=26,
                bold=True
            )

        elif shape.name == "insights_risk":

            shape.text = story["risk_insights"]

            format_text(
                shape,
                color=(30, 39, 97),
                size=18,
                bold=False
            )

        elif shape.name == "chart_risk":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide4.shapes.add_picture(
                "charts/risk_chart.png",
                left,
                top,
                width,
                height
            )

        elif shape.name == "icon_4":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide4.shapes.add_picture(
                "icons/risk_alert.png",
                left + width * 0.1,
                top + height * 0.1,
                width,
                height * 1.2
            )

    slide5 = ppt.slides[4]

    for shape in list(slide5.shapes):

        if shape.name == "title_5":

            shape.text = "Recommended Actions & Next Steps"

            format_text(
                shape,
                color=(255, 255, 255),
                size=26,
                bold=True
            )

        elif shape.name == "recommendations_text":

            shape.text = story["recommendations"]

            format_text(
                shape,
                color=(255, 255, 255),
                size=16,
                bold=False
            )

        elif shape.name == "closing_statement":

            shape.text = story["closing_statement"]

            format_text(
                shape,
                color=(202, 220, 252),
                size=18,
                bold=False,
                italic=True
            )

        elif shape.name == "icon_5":

            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height

            sp = shape._element
            sp.getparent().remove(sp)

            slide5.shapes.add_picture(
                "icons/lightbulb_action.png",
                left - width * 0.05,
                top,
                width * 1.1,
                height * 1.2
            )

    output_path = (
        "output/NovaRetail_Q2_2026_Executive_QBR_Final.pptx"
    )
    ppt.save(output_path)

    tool_context.state["deck_generated"] = True
    tool_context.state["deck_path"] = output_path

    return {
        "status": "success",
        "message": "Executive deck generated successfully.",
        "file_path": output_path
    }