import matplotlib.pyplot as plt

from tools.data_loader import load_data


def create_customer_chart():

    _, customer_df, _ = load_data()

    customer_data = customer_df.pivot(
        index="Quarter",
        columns="Region",
        values="NPS"
    )

    customer_data.plot(
        kind="line",
        marker="o",
        figsize=(10,6)
    )

    plt.title("NPS Trend by Region")
    plt.ylabel("NPS Score")
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

    plt.tight_layout()

    plt.savefig(
        "charts/customer_chart.png"
    )

    plt.close()

    print("Customer chart generated successfully!")


if __name__ == "__main__":
    create_customer_chart()