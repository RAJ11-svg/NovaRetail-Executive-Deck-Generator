from tools.data_loader import load_data

def generate_insights():

    performance_df, customer_df, risk_df = load_data()

    latest_quarter = "2026-Q2"

    latest_perf = performance_df[
        performance_df["Quarter"] == latest_quarter
    ]

    best_region = latest_perf.loc[
        latest_perf["Revenue_USD_M"].idxmax()
    ]

    worst_region = latest_perf.loc[
        latest_perf["Revenue_USD_M"].idxmin()
    ]

    print("\n===== PERFORMANCE INSIGHTS =====")

    print(
        f"Best Revenue Region: "
        f"{best_region['Region']} "
        f"({best_region['Revenue_USD_M']} M)"
    )

    print(
        f"Worst Revenue Region: "
        f"{worst_region['Region']} "
        f"({worst_region['Revenue_USD_M']} M)"
    )


if __name__ == "__main__":
    generate_insights()