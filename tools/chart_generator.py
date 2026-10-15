import matplotlib.pyplot as plt

from tools.data_loader import load_data

def create_revenue_chart():

    performance_df, _, _ = load_data()

    revenue_data = performance_df.pivot(
        index="Quarter",
        columns="Region",
        values="Revenue_USD_M"
    )

    revenue_data.plot(
        kind="bar",
        figsize=(10, 6)
    )

    plt.title("Revenue Trend by Region")
    plt.ylabel("Revenue (USD M)")
    plt.grid(True)
    ax = plt.gca()

    ax.title.set_color("#1E2761")

    ax.xaxis.label.set_color("#1E2761")

    ax.yaxis.label.set_color("#1E2761")

    ax.tick_params(axis='x', colors='#1E2761')

    ax.tick_params(axis='y', colors='#1E2761')

    legend = ax.get_legend()

    legend.get_title().set_color("#1E2761")

    for text in legend.get_texts():
        text.set_color("#1E2761")

    plt.savefig(
        "charts/revenue_chart.png",
        bbox_inches="tight"
    )

    plt.close()

    print("Revenue chart generated successfully!")


if __name__ == "__main__":
    create_revenue_chart()