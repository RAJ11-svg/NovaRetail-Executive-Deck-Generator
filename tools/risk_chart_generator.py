import matplotlib.pyplot as plt

from tools.data_loader import load_data


def create_risk_chart():

    _, _, risk_df = load_data()

    risk_data = risk_df.pivot(
        index="Quarter",
        columns="Region",
        values="Stockout_Rate_pct"
    )

    risk_data.plot(
        kind="bar",
      
        figsize=(10, 6)
    )

    plt.title("Stockout Rate Trend by Region")
    plt.ylabel("Stockout Rate (%)")
    plt.grid(True)

    ax = plt.gca()

    ax.title.set_color("#1E2761")

    ax.xaxis.label.set_color("#1E2761")

    ax.yaxis.label.set_color("#1E2761")

    ax.tick_params(axis='x', colors='#1E2761')

    ax.tick_params(axis='y', colors='#1E2761')

    legend = ax.get_legend()

    if legend:
        legend.get_title().set_color("#1E2761")

        for text in legend.get_texts():
            text.set_color("#1E2761")

    plt.tight_layout()

    plt.savefig(
        "charts/risk_chart.png"
    )

    plt.close()

    print("Risk chart generated successfully!")


if __name__ == "__main__":
    create_risk_chart()