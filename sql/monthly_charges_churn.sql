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
    END;