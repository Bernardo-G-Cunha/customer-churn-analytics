import pandas as pd
from src.database import run_query


def overall_churn():

    query = """
    SELECT
        COUNT(*) AS total_customers,

        SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) AS churned_customers,

        ROUND(
            AVG(
                CASE
                    WHEN Churn = 'Yes' THEN 1
                    ELSE 0
                END
            ) * 100,
            2
        ) AS churn_rate

    FROM customers
    """

    return run_query(query)


def churn_by_category(column: str) -> pd.DataFrame:

    query = f"""
    SELECT
        {column},
        COUNT(*) AS customers,
        ROUND(
            AVG(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100,
            2
        ) AS churn_rate
    FROM customers
    GROUP BY {column}
    ORDER BY churn_rate DESC
    """

    return run_query(query)


def churn_by_monthly_charge():

    query = """
    SELECT
        CASE
            WHEN MonthlyCharges < 25 THEN '15-24'
            WHEN MonthlyCharges < 35 THEN '25-34'
            WHEN MonthlyCharges < 50 THEN '35-49'
            WHEN MonthlyCharges < 65 THEN '50-64'
            WHEN MonthlyCharges < 80 THEN '65-79'
            WHEN MonthlyCharges < 95 THEN '80-94'
            WHEN MonthlyCharges < 110 THEN '95-109'
            ELSE '110+'
        END AS monthly_charge_group,

        COUNT(*) AS customers,

        ROUND(
            AVG(
                CASE
                    WHEN Churn = 'Yes' THEN 1
                    ELSE 0
                END
            ) * 100,
            2
        ) AS churn_rate

    FROM customers

    GROUP BY monthly_charge_group

    ORDER BY
        CASE monthly_charge_group
            WHEN '15-24' THEN 1
            WHEN '25-34' THEN 2
            WHEN '35-49' THEN 3
            WHEN '50-64' THEN 4
            WHEN '65-79' THEN 5
            WHEN '80-94' THEN 6
            WHEN '95-109' THEN 7
            WHEN '110+' THEN 8
        END
    """

    return run_query(query)


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