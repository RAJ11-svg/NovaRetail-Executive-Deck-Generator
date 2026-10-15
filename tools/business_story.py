from tools.data_loader import load_data
from google.adk.tools import ToolContext

def generate_story():

    performance_df, customer_df, risk_df = load_data()

    latest = "2026-Q2"

    latest_perf = performance_df[
        performance_df["Quarter"] == latest
    ]

    latest_customer = customer_df[
        customer_df["Quarter"] == latest
    ]

    latest_risk = risk_df[
        risk_df["Quarter"] == latest
    ]

    highest_capacity_region = latest_risk.loc[
    latest_risk["Warehouse_Capacity_Util_pct"].idxmax()
    ]["Region"]

    highest_capacity_util = latest_risk[
    "Warehouse_Capacity_Util_pct"
    ].max()

    highest_stockout_rate = latest_risk[
    "Stockout_Rate_pct"
    ].max()

    best_region = latest_perf.loc[
        latest_perf["Revenue_USD_M"].idxmax()
    ]["Region"]

    worst_region = latest_perf.loc[
        latest_perf["Revenue_USD_M"].idxmin()
    ]["Region"]

    top_nps_region = latest_customer.loc[
        latest_customer["NPS"].idxmax()
    ]["Region"]

    highest_risk_region = latest_risk.loc[
        latest_risk["Stockout_Rate_pct"].idxmax()
    ]["Region"]

    total_revenue = latest_perf[
        "Revenue_USD_M"
    ].sum()

    avg_nps = round(
        latest_customer["NPS"].mean(),
        1
    )
    total_revenue_display = f"${total_revenue / 1000:.2f}B"
    slide2_title = (
    f"{best_region} Leads Revenue While "
    f"{worst_region} Lags Behind"
    )
    slide3_title = (
    f"{top_nps_region} Leads Customer Experience"
    )
    slide4_title = (
    f"{highest_risk_region} Faces Rising Risk Exposure"
    )

    performance_insights = (
    f"• {best_region} remains the largest revenue contributor.\n"
    f"• {top_nps_region} shows strongest growth momentum.\n"
    f"• Europe remains stable across quarters.\n"
    f"• {worst_region} continues to decline."
    )

    customer_insights = (
    f"• {top_nps_region} achieved the highest NPS.\n"
    f"• Europe showed consistent customer satisfaction gains.\n"
    f"• North America remains stable with strong service levels.\n"
    f"• {highest_risk_region} experienced significant customer decline."
    )

    risk_insights = (
    f"• {highest_risk_region} shows highest operational risk.\n"
    f"• Fraud incidents continue increasing quarter-over-quarter.\n"
    f"• Return processing times are rising.\n"
    f"• {top_nps_region} warehouse utilization is approaching limits."
    )

    recommendations = (
    f"• Expand warehouse capacity in {highest_capacity_region} "
    f"before peak demand periods.\n\n"

    f"• Improve inventory planning and logistics execution "
    f"in {highest_risk_region}.\n\n"

    "• Strengthen fraud monitoring controls "
    "in higher-risk markets.\n\n"

    "• Reduce return-processing delays "
    "through operational automation."
    )

    closing_statement = (
    f"Prioritize growth investment in {top_nps_region} "
    f"while stabilizing operational performance in "
    f"{highest_risk_region}."
    )

    return {

    "best_region": str(best_region),

    "worst_region": str(worst_region),

    "top_nps_region": str(top_nps_region),

    "highest_risk_region": str(highest_risk_region),

    "total_revenue": int(total_revenue),

    "avg_nps": float(avg_nps),

    "slide2_title": str(slide2_title),

    "slide3_title": str(slide3_title),

    "slide4_title": str(slide4_title),

    "performance_insights": str(performance_insights),

    "customer_insights": str(customer_insights),

    "risk_insights": str(risk_insights),

    "recommendations": str(recommendations),

    "closing_statement": str(closing_statement),

    "highest_capacity_region": str(highest_capacity_region),

    "highest_capacity_util": float(highest_capacity_util),

    "highest_stockout_rate": float(highest_stockout_rate),

    "total_revenue_display": str(total_revenue_display),
}

def get_business_story(tool_context: ToolContext) -> dict:
    """Generate NovaRetail business story and save it in session state."""

    story = generate_story()

    tool_context.state["business_story"] = story
    tool_context.state["highest_risk_region"] = story["highest_risk_region"]
    tool_context.state["top_nps_region"] = story["top_nps_region"]
    tool_context.state["deck_generated"] = False

    return story

if __name__ == "__main__":

    story = generate_story()

    print(story)