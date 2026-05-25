import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def churn_by_tenure_contract(df: pd.DataFrame) -> pd.DataFrame:

    bins = [0, 12, 24, 48, float("inf")]

    labels = [
        "0-11",
        "12-23",
        "24-47",
        "48+"
    ]

    temp_df = df.copy()

    temp_df["tenure_group"] = pd.cut(
        temp_df["tenure"],
        bins=bins,
        labels=labels,
        right=False
    )

    result = (
        temp_df
        .groupby(["tenure_group", "Contract"])
        .agg(
            customers=("customerID", "count"),
            churn_rate=(
                "Churn",
                lambda x: round((x == "Yes").mean() * 100, 2)
            )
        )
        .reset_index()
    )

    return result


def plot_churn_by_tenure(df: pd.DataFrame):

    sns.lineplot(
        data=df,
        x="tenure",
        y="churn_rate",
        marker="o"
    )

    plt.title("Churn Rate by Customer Tenure")
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Churn Rate (%)")

    plt.show()


def plot_customers_by_tenure(df: pd.DataFrame):
    
    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="tenure",
        bins=20
    )

    plt.title("Customer Distribution by Tenure")
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Customers")

    plt.show()