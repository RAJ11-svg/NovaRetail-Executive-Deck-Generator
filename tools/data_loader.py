import pandas as pd

EXCEL_FILE = "data/novaretail_dataset.xlsx"


def load_data():
    """
    Load all sheets from Excel.
    Returns 3 DataFrames.
    """

    performance_df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Regional_Performance"
    )

    customer_df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Customer_Experience"
    )

    risk_df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Operational_Risk"
    )

    return performance_df, customer_df, risk_df


if __name__ == "__main__":

    performance, customer, risk = load_data()

    print("\n===== PERFORMANCE =====")
    print(performance.head())

    print("\n===== CUSTOMER =====")
    print(customer.head())

    print("\n===== RISK =====")
    print(risk.head())