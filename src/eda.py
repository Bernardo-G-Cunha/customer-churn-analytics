import pandas as pd

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