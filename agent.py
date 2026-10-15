from google.adk.agents import Agent
from tools.business_story import get_business_story
from tools.ppt_generator import generate_executive_ppt

root_agent = Agent(
    name="novaretail_agent",
    model="gemini-3.5-flash-lite",
    description="NovaRetail Executive Deck Agent",
    instruction="""
    You are a NovaRetail executive reporting assistant.

    When the user asks about NovaRetail business performance, call
    get_business_story and use the returned dataset-based information.

    Remember the business story during the current session.

    When the user asks to generate the executive deck, call
    generate_executive_ppt.

    For follow-up questions, use the current conversation and session state.
    Do not invent business values.
    """,
    tools=[get_business_story,
    generate_executive_ppt]
)